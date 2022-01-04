The resources in this repository are a continuation of the publication found in the footer and are associated with the following publication:

Scott, Jamie, Kristin Stock, Fraser Morgan, Brandon Whitehead, and David Medyckyj-Scott. “Automated Georeferencing of Antarctic Species.” In 11th International Conference on Geographic Information Science (GIScience 2021) - Part II, edited by Krzysztof Janowicz and Judith A. Verstegen, 208:13:1-13:16. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2021. https://doi.org/10.4230/LIPIcs.GIScience.2021.II.13.

**Current**
This project has been expanded in the following way:

1. Structure applied to code, input, and output
   The initial project held all notebooks, input files and output files in the same directory.  
   
   The following structure has been applied:
   
   - All notebooks are still in the parent directory
   - Input PDFs are placed in the PDFs directory
   - TagTog annotated PDFs should be bulk downloaded using the JSON formatting and placed in the ManuallyAnnotatedData directory
   - Initial SpreadSheets are found in the spreadsheet directory
   - NPYs are found in the NPY directory
   - All extractions are found in the matching Extracted[type] directory. For example, ExtractedText contains .txt files extracted from
     the PDFs
   - There is a Misc directory for random files from the original project that I did not find a use for
   
2. Training data expansion:

   The following notebooks were added:

  **ConvertTagTogData.ipynb**
   - Matches TagTog annotations files to the html files
   - Extracts annotations from the JSON files and text from the HTML files
   - Places both annotations.txt and text.txt into the "ExtractedAnnotatedData" folder in subdirectories that match:
     \\rootfolder\documentname\
 
   During this process the .html file will be converted to a .txt file that has the text as it appears in the PDF.
 
   The .txt file can be treated as per the extractedText .txt files, but with annotations for more accuracy and machine training.

3. The following is a breif overview of each original notebook and they're expansion:

   **ExtractingText.ipynb**
   This notebook takes a folder of .pdf's and extracts the PDFs texts to .txt files found in the ExtractedText folder. 
   Unfortunately imagick doesn't clean up it's temp files or release their file locks, so if you aren't careful you 
   will run out of memory or disk space. This is a bug within the ImageMagick Library.
   
   It was expanded from working with one hard coded file to a folder of PDFs. The data output was also sorted and structured.
   
   **GeoNames.ipynb**
   At the time of writing the notebook was corrupted (in the original project) 
   
   It is unnecessary as I contacted Jamie and all it does is make a text file that already exists
   
   **RecognisingSpeciesAndLocations**
   This notebook takes a folder of text files, as extracted by the ExtractingText.ipynb notebook, and identifies species and locations 
   within it.
   
   They are both added to the ExtractedLocations and ExtractedSpecies directories as spreadsheets in the ExtractedSpcies and 
   ExtractedLocations folders.
   
   It also makes a matrix of both and puts it in the ExtractedSLMatrix folder.
   
   It was expanded from working with one hard coded file to a folder of PDFs. The data output was also sorted and structured.
   
   **NERMetricsAndCreation.ipynb**
   This note book reads in TagTog annotation files and their matching .html files. It converts their .html file to text files and aligns
   the annotations to the text. 
   
   For each TagTog file it then scans the extracted species, locations and matrix folders for the matching spreadsheets, and creates metrics 
   on how accurate the extracted files are to the annotated files.

   This notebook was expanded to work with any number of PDFs, however because it was so intensive I have applied a couple of filters to 
   restrict the training to a set number of, or specificly named, PDFs



**Footer**
- - - - - - 
The resources in this repository are associated with the following publication:

Scott, Jamie, Kristin Stock, Fraser Morgan, Brandon Whitehead, and David Medyckyj-Scott. “Automated Georeferencing of Antarctic Species.” In 11th International Conference on Geographic Information Science (GIScience 2021) - Part II, edited by Krzysztof Janowicz and Judith A. Verstegen, 208:13:1-13:16. Leibniz International Proceedings in Informatics (LIPIcs). Dagstuhl, Germany: Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2021. https://doi.org/10.4230/LIPIcs.GIScience.2021.II.13.


### notes
The project had three main facets:
1) Extracting a clean text stream from legacy documents
2) Recognising mentions of species and locations within a document
3) Matching species and loactions mentions and modelling which pairs repesented a genuine species-was-found-at-location relationship

Notebooks contained in this repo and which step they belong to:
 ExtractingText.ipynb (1)
 GeoNames.ipynb (2) (intermediate preparation of GeoNames data)
 RecognisingSpeciesAndLocations.ipynb (2)
 NER Metrics and Matrix Creation.ipynb (2, 3)
 FeatureEngineering.ipynb (3)
 Building Models.ipynb (3)
 Visualisation.ipynb (reporting)

Due to time and scope, step was was paused and steps 2 and 3 were progressed using clean text streams copied directly from the docuemnts in the training set. 
