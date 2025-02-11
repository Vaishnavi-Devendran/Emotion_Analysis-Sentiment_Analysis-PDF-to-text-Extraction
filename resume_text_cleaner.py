import re

def remove_phone_numbers(text):
    pattern = r'\b(?:\+?91[-.\s]?)?[7-9]\d{9}\b'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

def remove_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


text_with_phone_numbers = '''
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                            ANKITA  ANKUSH   DHUMAL                               
                                  Aspiring Data Scientist                         
                    +91 8766036725 | LinkedIn | GitHub | ankitadhumal520@gmail.com
                                                                                  
                                                                                  
                                                                                  
          ABOUT                                                                  
                                                                                  
       An as piring Data Scientist with a Post-Graduation in Data Analytics from Imarticus Learning.
       I hav e specialized in Plus points of Process engineer, and enthusiastic about developing my
       skills in the field of Data Science. An engineering grad in Mechanical and graduated in the
       year 2018 with 3+ years of experience. Interested in pursuing a career in Data science and
       analy tics with the ability to identify the fine points of data, data exploration, data-mining,
       statis tical-analysis, data-visualization techniques.                      
       Exper ienced in team handling and skilled in public speaking, problem-solving, and decision
       makin g. Looking forward to utilizing these skills in the industry.        
          EDUCATION                                                              
                                                                                  
         2022-2023 Imarticus Learning                           Mumbai, India     
                  •  Post-Graduation in Data Analytics, NSDC certified            
                       o  Machine Learning using Python                           
                       o  SQL Programming                                         
                       o  Data Science with R                                     
                       o  Data Visualization using Power BI and Tableau           
                       o  Statistics Fundamentals                                 
                       o  Advanced Excel                                          
                       o  Deep Learning                                           
                       o  Big Data Analytics                                      
         2014 - 2018 St. John College of Engineering, MU University Mumbai, India 
                  •  Bachelor of Engineering in Mechanical (GPA – 6.02)           
                                                                                  
         2012 - 2014 Vartak College of Science, Maharashtra State Board Mumbai, India
                  •  Higher Secondary School Certificate (61.85%)                 
                                                                                  
         2010 – 2012 K.M.P.D. Highschool, Maharashtra State Board Mumbai, India   
                  •  Secondary School Certificate (84.80%)                        
                                                                                  
          CAPSTONE PROJECTS                                                      
                                                                                  
          Project Title “Car resale value prediction using Quikr data”           
          Project Outcomes • Problem Statement To predict the market value of a car based on various
                         factors like Company, Model name, Year, kms driven, fuel type.
                      •  Model using Linear Regression was able to predict the best resale value of used
                         cars with the accuracy of 90%                            
                      •  Algorithms used in models also include Decision tree, KNN, Random Forest. Lasso
                         and Ridge regularization techniques are also used.       
                                                                                  
          Project Title “IPL win probability prediction”                         
          Project Outcomes • Problem Statement To develop a predictive model that accurately predicts the
                         probability of a team winning an IPL cricket match.      
                      •  Using the Logistic Regression Model, the model was able to estimate the
                         likelihood of a team winning a match with about 82% accuracy.
                      •  Furthermore, KNN, Random Forest and SGD classifier were also used to solve the
                         problem statement and similar accuracies were found      
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  
          WORK EXPERIENCE (3 Years 10 Months)                                    
           Designation      EPU Manager                                          
           Company          Bombardier Transportation by Alstom (2021 Oct’ - 2022 Oct’)
           Roles & Responsibilities • Fabricated Car-body (Tram for Vienna) within stipulated time.
                             •  Implemented 7QC tools, 5S, Kaizen, Takt Line, Visual management.
                             •  Enhanced the product using root cause analysis tools.
                             •  Responsible for time management JIT & manpower management.
                             •  Hands on experience on tools for presenting project status and
                                insights to the client in Vienna, Austria         
           Designation      Process Engineer, Industrialization                  
           Company          Zobele India (P) Ltd., Daman & Diu. (2019 Apr’ - 2021 Sep’)
           Roles & Responsibilities • Involved in New Product Launch & Modification Process, PFMEA, Line
                                Layout making, Standard operating procedures (SOPs), Process Flow &
                                Work instructions, BO cost & Capex requirement.   
                             •  Improved quality using POKA-YOKE Principle & Load balancing.
                             •  Kaizen to improve work rate leading in 20% Cost saving for Vaporino
                                project.                                          
           Designation      Production Engineer, Manufacturing                   
           Company          Zobele India (P) Ltd., Daman & Diu. (2018 Dec’ - 2019 Mar’)
           Roles & Responsibilities • Planned and executed processes to achieve targeted output.
                             •  Labour efficiency analysis, Productivity, OLE, Overconsumption, OEE.
                             •  Kaizen solved for line layout redesigning to increase project PTC
                                capacity resulted in 40% output improvement.      
                                                                                  
          ADDITIONAL QUALIFICATIONS / CERTIFICATIONS                             
            •  Certification on Basics of Vehicle Dynamics and Fiber Molding.     
            •  Certification on Expert Course on Microsoft Excel.                 
            •  Certification on RC aircraft conducted by AerotriX                 
                                                                                  
          ACHIEVEMENTS/AWARDS                                                    
            •  SUPRA SAEINDIA 2018 -Team UDAAAN, Designed & Fabricated formula student car.
            •  FFS INDIA 2017- Automotive competitions, by FMAE, secured the position of 1st Runner up.
            •  International Series of Karting 2016 - Designed & Fabricated Go-kart for ISK2016.
          SKILLS                                                                 
                   Technical Skills       Proficiency  Soft Skills  Proficiency   
         Statistical Methods (Predictive Analysis, Hypothesis 7 Problem Solving 8 
         testing, PCA, Text Analytics)                                            
         Machine Learning (Classification, Regression, 7 Decision Making 8        
         Clustering techniques, Decision trees)                                   
         Natural Language Processing (NLTK, Spacy) 6 Leadership        8          
         Programming Languages (Python, SQL, MySQL) 7 Teamwork         8          
         Data Reporting tool (Tableau, Power BI) 7 Creativity          7          
         Microsoft (General Office and Presentation) 7 Written Communication 8    
         Process and Layout design, Lean Manufacturing Public Speaking            
         (AUTOCAD, SOLIDWORKS, eDrawings, DraftSight) 8                7          
                              *Levels of proficiency 1 to 5 – Basic; 6 to 8 – Intermediate; 9 to 10 – Advanced
          PERSONAL INFORMATION                                                   
         Address      Vasai, Mumbai, Maharashtra-401209                          
         Date of Birth 20/05/1996                                                
         Languages Known English (R/W/S), Marathi (R/W/S), Hindi (R/W/S), Gujarati (R/S)
         References      • Ms. Nikita Tandel                                     
                            o    AVP – Training & Development | Imarticus Learning
                            o    +91 9833283715 | nikita.tandel@imarticus.com     
                          • Mr. Bhagirath Thummar                                 
                            o    EPU Manager – Vienna | Alstom Group              
                            o    +91 9974700117 | bhagirath.thummar@alstomgroup.com
                                                                                  
                                                                                  
'''
cleaned_text = remove_phone_numbers(text_with_phone_numbers)
cleaned_text = remove_email_addresses(cleaned_text)
print(cleaned_text)