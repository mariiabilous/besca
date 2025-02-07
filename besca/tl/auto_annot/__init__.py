from ._auto_annot import read_data, read_raw, read_adata, merge_data, naive_merge, \
        scanorama_merge, remove_genes, intersect_genes, remove_nonshared, fit, linear_svm, \
        rbf_svm, sgd_svm, random_forest, logistic_regression, logistic_regression_ovr, logistic_regression_elastic,\
        adata_predict, predict,  adata_pred_prob, predict_proba, report

__all__ = ['read_data', 'read_raw', 'read_adata', 'merge_data', 'naive_merge', 'scanorama_merge', 'remove_genes', 'intersect_genes', 'remove_nonshared',
           'fit', 'linear_svm', 'rbf_svm', 'sgd_svm', 'random_forest', 'logistic_regression','logistic_regression_ovr',
            'logistic_regression_elastic', 'adata_predict', 'predict',  'adata_pred_prob', 'predict_proba' ,'report']
