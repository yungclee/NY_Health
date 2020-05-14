# NY Hospital Inpatient Discharge Data 

## Data Source
![enter image description here](https://phaboard.org/wp-content/uploads/New-York-State.png)
**Hospital Inpatient Discharges** data sets is one go the open data sets for general public provided by the state of New York (data.ny.gov). 

> "The Statewide Planning and Research Cooperative System (SPARCS)
> Inpatient De-identified File contains discharge level detail on
> patient characteristics, diagnoses, treatments, services, and charges.
> This data file contains basic record level detail for the discharge.
> The de-identified data file does not contain data that is protected
> health information (PHI) under HIPAA. The health information is not
> individually identifiable; all data elements considered identifiable
> have been redacted. For example, the direct identifiers regarding a
> date have the day and month portion of the date removed."


## Data Description

The de-identified file is currently available from 2008-2017. Each file contains around 2 millions entries, 34 columns including inpatient information: (only key variables are listed)
- **Demographic information**: gender, age group, race, and ethinticity.
- **Hopstial information**: hopital name, hospital service area, and hospital county.
- **Admission information**: type of admission, length of stay, 
- **Diagnosis information**: diagnosis code, drug code, severity of illness, risk of mortality, and treatment procedure.
- **Payment information**: total charges, total costs, insurance(medicare, medicaid, private insurance...)

## Goal 
Our goal is to build a **predictive model aim to estimate the final cost range for the inpatient** based on the symptoms and description from the user, for example, if a patient is admitted for giving birth what will be the estimated cost for this? If a patient is hospitalized due to pneumonia what will be the estimate cost?  

- **Target users**: Inpatients (currently restricted within New York State)
- **Exisiting product**: A similar product is available provided by Fair Health (https://www.fairhealthconsumer.org). It provides a 4-steps services to estimate the healthcare cost but it does not provide an overall estimation for all inpatient. The service from Fair Health requires more acknowlegement/ medical expertise such as knowing the *medical procedure name or ICD 10 code* in using the tool (see example below) and only single item can be estimated per time. 

> Example:  Female, 30s, giving birth to a baby. The inquiry on Fair
> Health will be as follow
> 1. Are you insured?
> 2. Where is your provider?
> 3. Select the type of care from tabs and categories
> 4. Prescription Simulator. (ICD 10 codes or Medical procedure)

 
The process is certainly not difficult but knowing what exact procedure or the precise treatment might not be for everyone, especially ICD-10 is a sophisticated and complex system for medical professionals knowing the exact code will certainly help getting a more accuracy and precise estimate but for general public use might not be the case.

## Current Progress
Simple exploratory data analysis is available (does not need to download the data, might need to install some module such as `sodapy` to query the data and `EDA` package for the code). We used systematic sampling to get the first 2000 entries across 2009-2017 as our EDA sample. 
The code utilize EDA module in python to generate fast Eda result to get some insight. 

## Challenges
After exploratory data analysis is done on small sample, we found some challenges/ known issues with modeling this data. 

- **Data Size**: The annual data contain around 2 million entries per file, which is around 900 MB per year. Normal computer hardware setup will be not enough to load data set in-memory. Possible solution will be batch processing or distributed computing. 
-  **Missing Values**: Across 2009-2017 the data format has slightly change, some information might be added or deleted for general public, potential solution includes using severe missing columns or imputation. ![Missing data from 2000 samples of each year](https://raw.githubusercontent.com/yungclee/NY_Health/master/Images/eda_missingdata.png)
-  **Imbalanced Data**:  There are multiple imbalanced categories in this data set, not only but including:	
	- **Gender-specific procedure**: some categories do not exist. Such as males are physiologically not capable of giving birth.  
	- **Emergency/underrepresented cases**: Some rare hospitalization including heart attack, gunshot wound. Such incidents may have impact on the admission type 

![enter image description here](https://raw.githubusercontent.com/yungclee/NY_Health/master/Images/eda_admission.png)

- **Demographic**: We can notice that the combinations of *[Race], [Ethinticity], and [Gender]*  is highly imbalanced in the dataset.
Possible solutions: include interaction term of gender and procedure, hierarchical modeling, or separate model for gender-sensitive procedure and conditions. 

![Ethinticity imbalance](https://raw.githubusercontent.com/yungclee/NY_Health/master/Images/eda_ethinticity_v2.png)
![Race imbalance](https://raw.githubusercontent.com/yungclee/NY_Health/master/Images/eda_race.png)

-  **Ambiguity in Payments**: from Eda, most patients' payment methods are medicare or medicaid, but the details from the medicare/medicaid is not listed from the data. 
-  **Procedure price/ Insurance coverage**: the data is time-sensitive, policies and insurance might have changed over the spam of the data. The charges from the hospital and the coverage form the insurance the inpatient use may act differently over time.  

## Questions?
Email Yung-Chun (Ray) Lee - yungclee@umich.edu .
