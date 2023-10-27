from __future__ import annotations

from liana.method.sc._liana_pipe import liana_pipe
from liana.utils import mdata_to_anndata

import anndata as an
from mudata import MuData
from pandas import DataFrame, concat
from typing import Optional
from tqdm import tqdm
import weakref


class MethodMeta:
    """
    A Class used to store Method Metadata
    """
    
    # initiate a list to store weak references to all instances
    instances = [] ## TODO separate instances for each child class
    
    def __init__(self,
                 method_name: str,
                 complex_cols: list,
                 add_cols: list,
                 fun,
                 magnitude: str | None,
                 magnitude_ascending: bool | None,
                 specificity: str | None,
                 specificity_ascending: bool | None,
                 permute: bool,
                 reference: str
                 ):
        """
        Parameters
        ----------
        method_name
            Name of the Method
        complex_cols
            Columns relevant for protein complexes
        add_cols
            Additional columns required by the method
        fun
            Interaction Scoring function
        magnitude
            Name of the `magnitude` Score (None if not present)
        magnitude_ascending
            Whether to rank `magnitude` in ascending manner (None if not relevant)
        specificity
            Name of the `specificity` Score if Present (None if not present)
        specificity_ascending
            Whether to rank `magnitude` in ascending manner  (None if not relevant)
        permute
            Whether it requires permutations
        reference
            Publication reference in Harvard style
        """
        self.__class__.instances.append(weakref.proxy(self))
        self.method_name = method_name
        self.complex_cols = complex_cols
        self.add_cols = add_cols
        self.fun = fun
        self.magnitude = magnitude
        self.magnitude_ascending = magnitude_ascending
        self.specificity = specificity
        self.specificity_ascending = specificity_ascending
        self.permute = permute
        self.reference = reference

    def describe(self):
        """Briefly described the method"""
        print(
            f"{self.method_name} uses `{self.magnitude}` and `{self.specificity}`"
            f" as measures of expression strength and interaction specificity, respectively"
        )

    def reference(self):
        """Prints out reference in Harvard format"""
        print(self.reference)

    def get_meta(self):
        """Returns method metadata as pandas row"""
        meta = DataFrame([{"Method Name": self.method_name,
                           "Magnitude Score": self.magnitude,
                           "Specificity Score": self.specificity,
                           "Reference": self.reference
                           }])
        return meta
    
    def by_sample(self, adata, sample_key, key_added='liana_res', inplace=True, verbose=False, **kwargs):
        """
        Run a method by sample.
        
        Parameters
        ----------
            adata 
                AnnData object to run the method on
            sample_key
                key in `adata.obs` to use for grouping by sample/context
            key_added
                key to store the results in `adata.uns` if `inplace` is True
            inplace
                whether to store the results in `adata.uns['liana_res']` or return a dataframe
            verbose
                Possible values: False, True, 'full', where 'full' will print the results for each sample,
                and True will only print the sample progress bar. Default is False.
            **kwargs
                keyword arguments to pass to the method
        
        Returns
        -------
        A pandas DataFrame with the results and a column sample if inplace is False, else None
        
        """
        
        if sample_key not in adata.obs:
            raise ValueError(f"{sample_key} was not found in `adata.obs`.")
        
        if adata.obs[sample_key].dtype.name != "category":
            (f"`{sample_key}` was assigned as a categorical.")
            adata.obs[sample_key] = adata.obs[sample_key].astype("category")
            
        if verbose == 'full':
            verbose = True
            full_verbose = True
        else:
            full_verbose = False
            
        samples = adata.obs[sample_key].cat.categories 
            
        adata.uns[key_added] = {}
        
        progress_bar = tqdm(samples, disable=not verbose)
        for sample in (progress_bar):
            if verbose:
                progress_bar.set_description(f"Now running: {sample}")

            temp = adata[adata.obs[sample_key]==sample].copy()

            sample_res = self.__call__(temp, inplace=False, verbose=full_verbose, **kwargs)

            adata.uns[key_added][sample] = sample_res

        liana_res = concat(adata.uns[key_added]).reset_index(level=1, drop=True).reset_index()
        liana_res = liana_res.rename({"index":sample_key}, axis=1)
        
        if inplace:
            adata.uns[key_added] = liana_res
        return None if inplace else liana_res


class Method(MethodMeta):
    """
    Ligand-Receptor Method Class
    """
    def __init__(self, _method):
        super().__init__(method_name=_method.method_name,
                         complex_cols=_method.complex_cols,
                         add_cols=_method.add_cols,
                         fun=_method.fun,
                         magnitude=_method.magnitude,
                         magnitude_ascending=_method.magnitude_ascending,
                         specificity=_method.specificity,
                         specificity_ascending=_method.specificity_ascending,
                         permute=_method.permute,
                         reference=_method.reference
                         )
        self._method = _method

    def __call__(self,
                 adata: an.AnnData,
                 groupby: str,
                 resource_name: str = 'consensus',
                 expr_prop: float = 0.1,
                 min_cells: int = 5,
                 base: float = 2.718281828459045,
                 supp_columns: list = None,
                 return_all_lrs: bool = False,
                 key_added: str = 'liana_res',
                 use_raw: Optional[bool] = True,
                 layer: Optional[str] = None,
                 de_method='t-test',
                 verbose: Optional[bool] = False,
                 n_perms: int = 1000,
                 seed: int = 1337,
                 resource: Optional[DataFrame] = None,
                 interactions=None,
                 mdata_kwargs = dict(),
                 inplace=True):
        """
        Parameters
        ----------
        adata
            Annotated data object.
        groupby
            The key of the observations grouping to consider.
        resource_name
            Name of the resource to be loaded and use for ligand-receptor inference.
        expr_prop
            Minimum expression proportion for the ligands/receptors (and their subunits) in the
            corresponding cell identities. Set to `0`, to return unfiltered results.
        min_cells
            Minimum cells per cell identity (`groupby`) to be considered for downstream analysis
        base
            Exponent base used to reverse the log-transformation of matrix. Note that this is
            relevant only for the `logfc` method.
        supp_columns
            Any additional columns to be added from any of the methods implemented in
            liana, or any of the columns returned by `scanpy.tl.rank_genes_groups`, each
            starting with ligand_* or receptor_*. For example, `['ligand_pvals', 'receptor_pvals']`.
            `None` by default.
        return_all_lrs
            Bool whether to return all LRs, or only those that surpass the `expr_prop`
            threshold. Those interactions that do not pass the `expr_prop` threshold will
            be assigned to the *worst* score of the ones that do. `False` by default.
        key_added
            Key under which the results will be stored in `adata.uns` if `inplace` is True.
        use_raw
            Use raw attribute of adata if present.
        layer
            Layer in anndata.AnnData.layers to use. If None, use anndata.AnnData.X.
        de_method
            Differential expression method. `scanpy.tl.rank_genes_groups` is used to rank genes
            according to 1vsRest. The default method is 't-test'. Only relevant if p-values
            are included in `supp_cols`
        verbose
            Verbosity flag
        n_perms
            Number of permutations for the permutation test. Note that this is relevant
            only for permutation-based methods - e.g. `CellPhoneDB`. If `None` is passed, 
            no permutation testing is performed.
        seed
            Random seed for reproducibility.
        resource
            Parameter to enable external resources to be passed. Expects a pandas dataframe
            with [`ligand`, `receptor`] columns. None by default. If provided will overrule
            the resource requested via `resource_name`
        interactions
            List of tuples with ligand-receptor pairs `[(ligand, receptor), ...]` to be used for the analysis.
            If passed, it will overrule the resource requested via `resource` and `resource_name`.
        mdata_kwargs
            Keyword arguments to be passed to `li.fun.mdata_to_anndata` if `adata` is an instance of `MuData`.
            If an AnnData object is passed, these arguments are ignored.
        inplace
            If true return `DataFrame` with results, else assign to `.uns`.

        Returns
        -------
            If ``inplace = False``, returns a `DataFrame` with ligand-receptor results
            Otherwise, modifies the ``adata`` object with the following key:
            - :attr:`anndata.AnnData.uns` ``[`key_added`]`` with the aforementioned DataFrame
        """
        if supp_columns is None:
            supp_columns = []
        
        if isinstance(adata, MuData):
            ad = mdata_to_anndata(adata, **mdata_kwargs, verbose=verbose)
        else:
            ad = adata

        liana_res = liana_pipe(adata=ad,
                               groupby=groupby,
                               resource_name=resource_name,
                               resource=resource,
                               interactions=interactions,
                               expr_prop=expr_prop,
                               min_cells=min_cells,
                               supp_columns=supp_columns,
                               return_all_lrs=return_all_lrs,
                               base=base,
                               de_method=de_method,
                               verbose=verbose,
                               _score=self._method,
                               n_perms=n_perms,
                               seed=seed,
                               use_raw=use_raw,
                               layer=layer,
                               )
        if inplace:
            adata.uns[key_added] = liana_res
        return None if inplace else liana_res
        

def _show_methods(methods):
    return concat([method.get_meta() for method in methods])
