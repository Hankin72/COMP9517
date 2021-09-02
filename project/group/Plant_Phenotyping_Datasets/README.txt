Plant Phenotyping Datasets
Version: 1.0
Date:    4 December 2015
Website: http://www.plant-phenotyping.org/datasets



I. INTRODUCTION

We present a collection of benchmark datasets in the context of plant phenotyping. We provide annotated imaging data and suggest suitable evaluation criteria for plant/leaf segmentation, detection, tracking as well as classification and regression problems. The data is available together with ground truth segmentations and further annotations and metadata.

The Plant Phenotyping Datasets are intended for the development and evaluation of computer vision and machine learning algorithms such as (in parentheses we point to general category of computer vision problems that these datasets can also be used for):
- plant detection and localization (multi-instance detection/localization);
- plant segmentation (foreground to background segmentation);
- leaf detection, localization, and counting (multi-instance detection, object counting);
- leaf segmentation (multi-instance segmentation);
- leaf tracking (multi-instance segmentation);
- boundary estimation for multi-instance segmentation (boundary detectors);
- classification and regression of mutants and treatments (general classification recognition).
The data can be used by scientists that already work in related fields but also from general computer vision scientists that work in related computer vision problems. No matter what, testing your algorithms on these data, you help us improve the state-of-the-art in phenotyping and feed the world one image at a time.



II. STRUCTURE OF THE DATASET

Image data are divided into three groups:
- Plant: color images of single plants accompanied by annotations (leaf segmentation masks, leaf bounding boxes, leaf centers, leaf boundaries) and possibly metadata;
- Stacks: time series of single plant images accompanied by time-consistent annotations (leaf segmentation masks, leaf bounding boxes);
- Tray: color images of trays including multiple plants accompanied by annotations (plant segmentation masks, plant bounding boxes).

The mapping between vision tasks and files in the dataset is as follows.

(1) Plant detection and localization
    Ara2012: Tray/Ara2012/*_rgb.png (16 files), Tray/Ara2012/*_bbox.csv (16 files);
    Ara2013 (Canon): Tray/Ara2013-Canon/*_rgb.png (27 files), Tray/Ara2013-Canon/*_bbox.csv (27 files);
    Ara2013 (RPi): Tray/Ara2013-RPi/*_rgb.png (27 files), Tray/Ara2013-RPi/*_bbox.csv (27 files).

(2) Plant segmentation
    Ara2012: Tray/Ara2012/*_rgb.png (16 files), Tray/Ara2012/*_fg.png (16 files);
    Ara2013 (Canon): Tray/Ara2013-Canon/*_rgb.png (27 files), Tray/Ara2013-Canon/*_fg.png (27 files).

(3) Leaf segmentation
    Ara2012: Plant/Ara2012/*_rgb.png (120 files), Plant/Ara2012/*_label.png (120 files);
    Ara2013 (Canon): Plant/Ara2013-Canon/*_rgb.png (165 files), Plant/Ara2013-Canon/*_label.png (165 files);
    Tobacco: Plant/Tobacco/*_rgb.png (62 files), Plant/Tobacco/*_label.png (62 files).

(4) Leaf detection
    Ara2012: Plant/Ara2012/*_rgb.png (120 files), Plant/Ara2012/*_bbox.csv (120 files);
    Ara2013 (Canon): Plant/Ara2013-Canon/*_rgb.png (165 files), Plant/Ara2013-Canon/*_bbox.csv (165 files);
    Tobacco: Plant/Tobacco/*_rgb.png (62 files), Plant/Tobacco/*_bbox.csv (62 files).

(5) Leaf counting
    Ara2012: Plant/Ara2012/*_rgb.png (120 files), Plant/Ara2012/*_centers.png (120 files), Plant/Ara2012/Leaf_counts.csv;
    Ara2013 (Canon): Plant/Ara2013-Canon/*_rgb.png (165 files), Plant/Ara2013-Canon/*_centers.png (165 files), Plant/Ara2013-Canon/Leaf_counts.csv;
    Tobacco: Plant/Tobacco/*_rgb.png (62 files), Plant/Tobacco/*_centers.png (62 files), Plant/Tobacco/Leaf_counts.csv.

(6) Leaf tracking
    Ara2012: Stacks/Ara2012/stack_* (4 directories);
    Ara2013 (Canon): Stacks/Ara2013-Canon/stack_* (8 directories).

(7) Boundary estimation
    Ara2012: Plant/Ara2012/*_rgb.png (120 files), Plant/Ara2012/*_boundaries.png (120 files);
    Ara2013 (Canon): Plant/Ara2013-Canon/*_rgb.png (165 files), Plant/Ara2013-Canon/*_boundaries.png (165 files);
    Tobacco: Plant/Tobacco/*_rgb.png (62 files), Plant/Tobacco/*_boundaries.png (62 files).

(8) Classification and regression
    Ara2013 (Canon): Plant/Ara2013-Canon/*_rgb.png (165 files), Plant/Ara2013-Canon/Metadata.csv;
    Tobacco: Plant/Tobacco/*_rgb.png (62 files), Plant/Tobacco/Metadata.csv.

Additional notes on the CSV files.
CSV files containing leaf or plant bounding box annotations (*_bbox.csv) report bounding box coordinates of the four corners in the following order: c1x, c1y, c2x, c2y, c3x, c3y, c4x, c4y.
CSV files containing leaf counts (Leaf_counts.csv) report: file ID, number of leaves.
CSV files containing plant metadata (Metadata.csv) report: file ID, genotype, treatment, time after germination (hours).



III. TERMS AND CONDITIONS

Access to the data implies that the user also agrees to the following terms and conditions:
1. Copyright and ownership of images/data remain of the owners and dataset administrators (M. Minervini, H. Scharr, S.A. Tsaftaris).
2. The owners reserve the right to amend the terms and conditions.
3. Data cannot be used for commercial use including but not limited to: demonstrating the efficiency of and testing commercial systems, using screenshots from the database in advertisements, selling data from the database.
4. Data can be used for academic purposes in the context of developing and evaluating algorithms.
5. Publications using said data must cite the dataset and relevant paper(s) as indicated in Sec. IV. Publications include journal/conference articles, technical reports, institutional or mass managed repositories (e.g., arXiv), posters, books, conference presentations, seminars, etc.
6. Studies in plant physiology and to discover new biological meaning and findings are not encouraged using these data.
7. Data and annotations cannot be distributed and reproduced with the exception of small excerpts (such as scaled down or cropped example images) in publications as long as said publication conforms to point 4 above.
8. Data and annotations cannot be bundled with other datasets (and re-leased) without consent of the dataset owners.
9. Data and annotations cannot be used to support challenges/competitions without consent of the dataset owners.
10. Disclaimer: The data and annotations are given as is without any warranty from the dataset owners. The owners cannot be held accountable do not hold any responsibility and cannot be held responsible.



IV. CITATION

If you use this dataset in your research, it is mandatory to reference our website (http://www.plant-phenotyping.org/datasets) and cite the following article:

Massimo Minervini, Andreas Fischbach, Hanno Scharr, Sotirios A. Tsaftaris, Finely-grained annotated datasets for image-based plant phenotyping, Pattern  Recognition Letters (2015), doi: 10.1016/j.patrec.2015.10.013

@ARTICLE{Minervini2015PRL,
  author = {Massimo Minervini and Andreas Fischbach and Hanno Scharr and Sotirios A. Tsaftaris},
  title = {Finely-grained annotated datasets for image-based plant phenotyping},
  journal = {Pattern Recognition Letters},
  pages = {1-10},
  year = {2015}
}



V. CONTACTS

Please feel free to contact us with any feedback, comments, or questions. If you have any corrections in annotations please do let us know. If you want to be kept updated on the progress of the Plant Phenotyping Datasets, please send us an email and we will keep you posted.

- Massimo Minervini, IMT Institute for Advanced Studies, Lucca, Italy (massimo.minervini@imtlucca.it)
- Sotirios A. Tsaftaris, University of Edinburgh, UK (S.Tsaftaris@ed.ac.uk)
- Hanno Scharr, IBG-2, Forschungszentrum Juelich, Juelich, Germany (H.Scharr@fz-juelich.de)
