# Land Cover Change in the Kolyma Region: A CNN-Based Arctic Vegetation Analysis

**By Adam Koplik and Professor Heather Kropp**

## Overview  
Between Summer 2023 and Spring 2024, I conducted research with Professor Heather Kropp examining how land cover in the Kolyma lowland region of northeastern Siberia has changed between the 1970s and today. The project focused on classifying historical and contemporary satellite imagery to detect changes in tree, shrub, water, and low-density forest cover, with a specific focus on the expansion of tall shrubs linked to climate change.

We built a Convolutional Neural Network (CNN) to classify land cover types from high-resolution imagery and compared the classifications from 1971 and 2020 to measure long-term changes.

## Project Scope  

- Collected and processed **1971 KeyHole-9 satellite imagery** and **2020 WorldView-3 imagery** for a 171 km² region of the Kolyma lowland.
- Created a training dataset of 400 image tiles, manually classifying pixels into four categories: trees, water, shrubs, and low-density forest.
- Developed and trained a **Convolutional Neural Network (CNN)** using **Keras** to classify land cover types.
- Applied the trained model to the full imagery set, producing mosaicked land cover predictions for both time periods.
- Measured changes in vegetation cover between 1971 and 2020 and analyzed spatial patterns relative to nearby water bodies and pre-existing vegetation.

## Methods  

- **ArcGIS Pro** for viewing and prepping satellite imagery.
- **Keras** (Python) for CNN model creation and training.
- Created training masks by manually drawing labeled polygons for each land cover class.
- Exported training images and masks, trained the model, and applied predictions to full mosaicked images.

## Key Results  

- Found a net increase of **14 km² in shrubland cover** since 1971.
- Taiga (tree) cover remained relatively stable overall but exhibited highly heterogeneous, patchy changes across the landscape.
- Vegetation changes were strongly clustered near water bodies and in proximity to existing shrubland.
- Moderate-resolution greenness indices from existing datasets failed to capture this fine-scale heterogeneity.
- Demonstrated the effectiveness of high-resolution imagery paired with machine learning models for monitoring Arctic land cover changes.

## Tools and Technologies  

- ArcGIS Pro  
- Keras (Python)  
- TensorFlow  
- Jupyter Notebook  
- WorldView-3 and KeyHole-9 satellite imagery  

## Takeaways  

This project demonstrated the potential for high-resolution remote sensing and machine learning models to reveal nuanced patterns of vegetation change in remote Arctic regions. It highlighted both the ecological importance of shrub expansion in permafrost landscapes and the limitations of moderate-resolution greenness indices for tracking fine-scale vegetative transitions.

## Full Poster and Abstract  

- [Download Summer 2023 Research Poster (PDF)](summer_research_poster.pdf)  
- [Download Abstract PDF (for AGU submission)](land_cover_abstract.pdf)

## Acknowledgements  

Special thanks to Professor Heather Kropp for her mentorship throughout this project and to the Hamilton College Environmental Studies Department for supporting the research.
