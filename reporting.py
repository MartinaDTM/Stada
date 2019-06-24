# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:07:06 2019

@author: Toni
"""
def initialize_columns ():
    INITIATIVE_COLUMNS = ['id',
     'load_id',
     'initiative_id',
     'initiative_name',
     'stage',
     'weekly_status',
     'card_type',
     'cost_type',
     'geography_triggered',
     'report',
     'fte_type',
     'description_of_initiative_and_assumption_used',
     'what_is_the_money_step_-_how_does_this_add_value',
     'workstream',
     'sub-workstream',
     'initiative_owner',
     'initiative_owner_back-up',
     'initiative_lead_approver',
     'sponsor_approver',
     'finance_approver',
     'to_approver',
     'recurring_cash_impact',
     'one-time_cash_impact',
     'implementation_cost',
     'l1_actual_date',
     'l2_actual_date',
     'l3_planned_date',
     'l3_actual_date',
     'l3_forecast_date',
     'l3_latest_estimated_date',
     'l4_planned_date',
     'l4_actual_date',
     'l4_forecast_date',
     'l4_latest_estimated_date',
     'l5_actual_date',
     'sub_for_l2_approv_date',
     'sub_for_l3_approv_date',
     'sub_for_l4_approv_date',
     'sub_for_l5_approv_date']
    
    MILESTONES_COLUMNS = ['id',
     'load_id',
     'milestone_id',
     'initiative_id',
     'initiative_name',
     'milestone_name',
     'status',
     'planning_summary',
     'planning_check',
     'owner',
     'start_date',
     'end_date']
    
    
    IMPACTS_COLUMNS = ['id',
     'load_id',
     'initiative_id',
     'impact_id',
     'initiative_name',
     'Stage',
     'Weekly status',
     'Workstream',
     'Initiative owner',
     'L4 planned date',
     'Impact geography > Country',
     'Impact status',
     'Metric > Metric Category',
     'Metric > Metric',
     'Allocation area > Workstream',
     'Allocation area > Sub-Workstream',
     'purpose',
     'Run Rate',
     '2017_10_01',
     '2017_11_01',
     '2017_12_01',
     '2018_01_01',
     '2018_02_01',
     '2018_03_01',
     '2018_04_01',
     '2018_05_01',
     '2018_06_01',
     '2018_07_01',
     '2018_08_01',
     '2018_09_01',
     '2018_10_01',
     '2018_11_01',
     '2018_12_01',
     '2019_01_01',
     '2019_02_01',
     '2019_03_01',
     '2019_04_01',
     '2019_05_01',
     '2019_06_01',
     '2019_07_01',
     '2019_08_01',
     '2019_09_01',
     '2019_10_01',
     '2019_11_01',
     '2019_12_01',
     '2020_01_01',
     '2020_02_01',
     '2020_03_01',
     '2020_04_01',
     '2020_05_01',
     '2020_06_01',
     '2020_07_01',
     '2020_08_01',
     '2020_09_01',
     '2020_10_01',
     '2020_11_01',
     '2020_12_01',
     '2021_01_01',
     '2021_02_01',
     '2021_03_01',
     '2021_04_01',
     '2021_05_01',
     '2021_06_01',
     '2021_07_01',
     '2021_08_01',
     '2021_09_01',
     '2021_10_01',
     '2021_11_01',
     '2021_12_01',
#     '2022_01_01',
#     '2022_02_01',
#     '2022_03_01',
#     '2022_04_01',
#     '2022_05_01',
#     '2022_06_01',
#     '2022_07_01',
#     '2022_08_01',
#     '2022_09_01',
#     '2022_10_01',
#     '2022_11_01',
#     '2022_12_01',
#     '2023_01_01',
#     '2023_02_01',
#     '2023_03_01',
#     '2023_04_01',
#     '2023_05_01',
#     '2023_06_01',
#     '2023_07_01',
#     '2023_08_01',
#     '2023_09_01',
#     '2023_10_01',
#     '2023_11_01',
#     '2023_12_01',
 ]
    
    KPI_COLUMNS = ['id',
     'load_id',
     'kpi_id',
     'initiative_id',
     'initiative_name',
     'measure',
     'unit',
     'purpose',
     '2017_10_01',
     '2017_11_01',
     '2017_12_01',
     '2018_01_01',
     '2018_02_01',
     '2018_03_01',
     '2018_04_01',
     '2018_05_01',
     '2018_06_01',
     '2018_07_01',
     '2018_08_01',
     '2018_09_01',
     '2018_10_01',
     '2018_11_01',
     '2018_12_01',
     '2019_01_01',
     '2019_02_01',
     '2019_03_01',
     '2019_04_01',
     '2019_05_01',
     '2019_06_01',
     '2019_07_01',
     '2019_08_01',
     '2019_09_01',
     '2019_10_01',
     '2019_11_01',
     '2019_12_01',
     '2020_01_01',
     '2020_02_01',
     '2020_03_01',
     '2020_04_01',
     '2020_05_01',
     '2020_06_01',
     '2020_07_01',
     '2020_08_01',
     '2020_09_01',
     '2020_10_01',
     '2020_11_01',
     '2020_12_01',
     '2021_01_01',
     '2021_02_01',
     '2021_03_01',
     '2021_04_01',
     '2021_05_01',
     '2021_06_01',
     '2021_07_01',
     '2021_08_01',
     '2021_09_01',
     '2021_10_01',
     '2021_11_01',
     '2021_12_01',
#     '2022_01_01',
#     '2022_02_01',
#     '2022_03_01',
#     '2022_04_01',
#     '2022_05_01',
#     '2022_06_01',
#     '2022_07_01',
#     '2022_08_01',
#     '2022_09_01',
#     '2022_10_01',
#     '2022_11_01',
#     '2022_12_01',
#     '2023_01_01',
#     '2023_02_01',
#     '2023_03_01',
#     '2023_04_01',
#     '2023_05_01',
#     '2023_06_01',
#     '2023_07_01',
#     '2023_08_01',
#     '2023_09_01',
#     '2023_10_01',
#     '2023_11_01',
#     '2023_12_01',
  ]
    return INITIATIVE_COLUMNS,MILESTONES_COLUMNS,IMPACTS_COLUMNS,KPI_COLUMNS


def filter_load_id(data,lid):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
        Subset of table with the specific input load id
    """
    new_data=data.copy()
    new_data=new_data[new_data.load_id==lid]

    return new_data


def loading_table(table_name,connection):
    """
    Parameters
    ----------
    table_name : str
        Name of the table which needs to be loaded
    connection : object
        Which sqlalchamy object to be used to extract the table
    
    Returns
    ----------
    table: DataFrame
        Extracted the table with table_name(given as input) from the specific database
        
    """
    print('{} {}'.format("SELECT * FROM", table_name))
    table=pd.read_sql('{} {}'.format("SELECT * FROM", table_name),con=connection)
    table=filter_load_id(table,table.load_id.max())
    return table


def filter_category(imp,filter_string):
    """
    Parameters
    ----------
    imp : DataFrame
        Table to filter categories in
    filter_string : str
        String to compare category with 
    
    Returns
    ----------
    out: DataFrame
        Segmented Data Frame for each category for filter string
    """
    
    data=imp.copy()
    out=data[data.metric_metric_category==filter_string]
    return out

  
def loading_tables(stage):
    """
    Parameters
    ----------
    stage : object
        Data Base object

    
    Returns
    ----------
    impacts: DataFrame
        Impacts Table
    kpi: DataFrame
        KPI Table
    milestones: DataFrame
        Milestones Table
    initiatives: DataFrame
        Initiatives Table
    """
    
    print('Loading Tables')
    impacts=loading_table('impacts',stage)
    kpi=loading_table('kpidetails',stage)
    milestones=loading_table('milestones',stage)
    initiatives=loading_table('initiatives',stage)
    
    return impacts,kpi,milestones,initiatives

def change_the_impact_status (impacts):
    """
    This function changes the "Impact Status" column if: 
        * 'P&L effective savings' = "P&L"
        * 'Implemented savings' = 'Implemented'
    Also the column name "Impact Status" is changed to "saving_type"
    
    Parameters
    ----------
    impacts : DataFrame
        Table ( by default needs to be the impacts table)

    Returns
    ----------
    impacts: DataFrame
        Changed input table
    """
    impacts.loc[impacts['Impact status']=='P&L effective savings','Impact status']="P&L"
    impacts.loc[impacts['Impact status']=='Implemented savings','Impact status']="Implemented"
    impacts.rename(columns={'Impact status':'savings_type'},inplace=True)
    return impacts


def check_new_table_loaded(engine,initiatives):
    
    """
    Check if new table is uploaded
        - or else we will have multiple instances with the same data and reports will ne wrong
    Parameters
    ----------
    engine : object
        Object for the layer in the DB
    initiatives : Data Frame 
        Initiatives Table
    
    Raises:
    ----------
    Value Error ("Before running the code, please upload new data with WAVE Import Tool")
    """
    initiatives_integ=loading_table('initiatives',engine)
    
    if initiatives_integ.load_id.max()==initiatives.load_id.max():
        raise ValueError("Before running the code, please upload new data with WAVE Import Tool")

 
def pre_process_impact_columns(impacts):
    """
    we are spliting the table according to the dabase documentation
    'id', 'load_id', 'initiative_id', 'impact_id' is the 
    key making date colums as one column with date values
    
    Parameters
    ----------
    impacts : DataFrame
        Table containing Impacts data

    Returns
    ----------
    impacts: DataFrame
    """
    imp_cols=impacts.columns.tolist()
    imp_cols=[s.replace(' ','_') for s in imp_cols]
    imp_cols=[s.replace('_>','') for s in imp_cols]
    imp_cols=[s.replace('-','_') for s in imp_cols]
    imp_cols=[s.lower() for s in imp_cols]
    impacts.columns=imp_cols
    return impacts


def subsetting_impacts(impacts):
    """
    for all the initiatives that are in L1 or L2, if they have a positive run rate value, but all
    of the monthly values (i.e. Jan 2018 - Dec 2021) are zero, the last monthly value (Dec 2021) 
    should be overwritten with the run rate value.
    If the initiative is in stage L1, all of the Forecast values are to be overwritten with Plan values.
    
    If the initiative is in stage L1, all of the Forecast values are to be overwritten with Plan values.
        Impacts temp 2 is the table where: 
        1. stage  = L1 and stage  = Submitted for L2 approval
        2. purpose = Plan 
        3. make the id and add 2 to all of the rows. 
  
    Impacts temp 2 is the table where: 
        1. stage  != L1 and stage  != Submitted for L2 approval
        2. purpose != 'Forecast'
        3. add impacts 2 to impact 3 
    

    Parameters
    ----------
    impacts : DataFrame
        Table containing impacts data

    Returns
    ----------
    impacts: DataFrame
    """
    
    impacts_temp = impacts.copy()
    # make a checksum for all of the dates 
    impacts_temp['checksum'] = impacts_temp.iloc[:, -51:].sum(axis = 1)
    conditions = [
        (((impacts_temp['stage'] == 'L1') |
                (impacts_temp['stage'] == 'L2') |
                (impacts_temp['stage'] == 'Submitted for L2 approval')|
                (impacts_temp['stage'] == 'Submitted for L3 approval')) 
         & (impacts_temp['run_rate'] > 0) & (impacts_temp['checksum'] == 0))
    ]
    choices = [impacts_temp['run_rate']]
    
    impacts_temp['2021_12_01'] = np.select(conditions, choices, default = impacts_temp['2021_12_01'])
    
    # DELETE Checksum 
    impacts = impacts_temp.drop(['checksum'], axis = 1)
    
    impacts_temp2 = impacts.copy()
    
    impacts_temp2 = impacts_temp2[(impacts_temp['stage'] == 'L1') | (impacts_temp['stage'] == 'Submitted for L2 approval')]
    impacts_temp2 = impacts_temp2[impacts_temp2['purpose'] == 'Plan']
    
    impacts_temp2['purpose'] = impacts_temp2['purpose'].str.replace('Plan', 'Forecast')
    impacts_temp2['id'] = impacts_temp2['id']+2
    
    
    impacts_temp3 = impacts.copy()
    impacts_temp3 = impacts_temp3[((impacts_temp3['stage'] != 'L1') & (impacts_temp3['stage'] != 'Submitted for L2 approval')) | (impacts_temp3['purpose'] != 'Forecast')]
    
    impacts_temp4 = impacts_temp2.append(impacts_temp3)
    
    impacts = impacts_temp4.copy()
    
    return impacts



def create_impact_description_and_store(impacts,new_integration):
    
    """
    Create impact description table and store it in the database
    Parameters
    ----------
    impacts : DataFrame
        Table containing impacts Data 
    new_integration : object
        Connection to DB
    
    Returns
    ----------
    impacts_description: DataFrame
    """
    
    impacts_description=impacts[['id', 'load_id', 'initiative_id', 'impact_id', 'workstream', 
                         'impact_geography_country', 'metric_metric_category',
                          'metric_metric', 'allocation_area_workstream',
                         'allocation_area_sub_workstream', 'run_rate',"savings_type"]]
    
    
    impacts_description.to_sql(name='impacts',con=new_integration,index=False,if_exists='append')
    print('input description stored')
    return impacts_description

def create_and_store_impact_value(impacts,new_integration):
    
    """
    Create and Store impact values. 
    Forecasts are now overwritten with Plans.
    Parameters
    ----------
    impacts : DataFrame
        Table containing impacts data 
    new_integration : object
        Connection to DB
    
    Returns
    ----------
    impacts_value: DataFrame
    """
    impacts_value=impacts[['id', 'load_id', 'impact_id','purpose',"savings_type", '2017_10_01',
           '2017_11_01', '2017_12_01', '2018_01_01', '2018_02_01', '2018_03_01',
           '2018_04_01', '2018_05_01', '2018_06_01', '2018_07_01', '2018_08_01',
           '2018_09_01', '2018_10_01', '2018_11_01', '2018_12_01', '2019_01_01',
           '2019_02_01', '2019_03_01', '2019_04_01', '2019_05_01', '2019_06_01',
           '2019_07_01', '2019_08_01', '2019_09_01', '2019_10_01', '2019_11_01',
           '2019_12_01', '2020_01_01', '2020_02_01', '2020_03_01', '2020_04_01',
           '2020_05_01', '2020_06_01', '2020_07_01', '2020_08_01', '2020_09_01',
           '2020_10_01', '2020_11_01', '2020_12_01', '2021_01_01', '2021_02_01',
           '2021_03_01', '2021_04_01', '2021_05_01', '2021_06_01', '2021_07_01',
           '2021_08_01', '2021_09_01', '2021_10_01', '2021_11_01', '2021_12_01']]
    
    
    ids=['id', 'load_id', 'impact_id','savings_type','purpose']
    val=['2017_10_01',
           '2017_11_01', '2017_12_01', '2018_01_01', '2018_02_01', '2018_03_01',
           '2018_04_01', '2018_05_01', '2018_06_01', '2018_07_01', '2018_08_01',
           '2018_09_01', '2018_10_01', '2018_11_01', '2018_12_01', '2019_01_01',
           '2019_02_01', '2019_03_01', '2019_04_01', '2019_05_01', '2019_06_01',
           '2019_07_01', '2019_08_01', '2019_09_01', '2019_10_01', '2019_11_01',
           '2019_12_01', '2020_01_01', '2020_02_01', '2020_03_01', '2020_04_01',
           '2020_05_01', '2020_06_01', '2020_07_01', '2020_08_01', '2020_09_01',
           '2020_10_01', '2020_11_01', '2020_12_01', '2021_01_01', '2021_02_01',
           '2021_03_01', '2021_04_01', '2021_05_01', '2021_06_01', '2021_07_01',
           '2021_08_01', '2021_09_01', '2021_10_01', '2021_11_01', '2021_12_01']
    
    
    impacts_value=pd.melt(impacts_value, id_vars=ids, value_vars=val,var_name='date',value_name='impact_value')
    
    impacts_value['date']=pd.to_datetime(impacts_value.date,format='%Y_%m_%d').dt.date  
    
    
    impacts_value.to_sql(name='impacts_value',con=new_integration,index=False,if_exists='append')
    
    print('impact_value stored in the database')
    return impacts_value

def create_and_store_kpi_descriptions(kpi,new_integration):
    """
    Create and store KPI description 
    Parameters
    ----------
    kpi : DataFrame
        Table containing KPI data
    new_integration : object
        
        Connection to the DB    
    Returns
    ----------
    None : 
    print('KPI_descrition stored in the database')
    """
    
    kpi_description=kpi[['id', 'load_id', 'initiative_id', 'kpi_id', 'measure', 'unit']]
    kpi_description.to_sql(name='kpi',con=new_integration,index=False,if_exists='append')
    return print('KPI_descrition stored in the database')
    
def create_and_store_kpi_value(kpi,new_integration):
    """
    Parameters
    ----------
    kpi : DataFrame
        Table containing Load_id as a column
    new_integration : Object
        Connection to the DB 
    
    Returns
    ----------
    None
    """
    
    kpi_value=kpi[['id', 'load_id', 'kpi_id','purpose', '2017_10_01',
           '2017_11_01', '2017_12_01', '2018_01_01', '2018_02_01', '2018_03_01',
           '2018_04_01', '2018_05_01', '2018_06_01', '2018_07_01', '2018_08_01',
           '2018_09_01', '2018_10_01', '2018_11_01', '2018_12_01', '2019_01_01',
           '2019_02_01', '2019_03_01', '2019_04_01', '2019_05_01', '2019_06_01',
           '2019_07_01', '2019_08_01', '2019_09_01', '2019_10_01', '2019_11_01',
           '2019_12_01', '2020_01_01', '2020_02_01', '2020_03_01', '2020_04_01',
           '2020_05_01', '2020_06_01', '2020_07_01', '2020_08_01', '2020_09_01',
           '2020_10_01', '2020_11_01', '2020_12_01', '2021_01_01', '2021_02_01',
           '2021_03_01', '2021_04_01', '2021_05_01', '2021_06_01', '2021_07_01',
           '2021_08_01', '2021_09_01', '2021_10_01', '2021_11_01', '2021_12_01']]
    
    ids=['id', 'load_id', 'kpi_id','purpose']
    val=['2017_10_01',
           '2017_11_01', '2017_12_01', '2018_01_01', '2018_02_01', '2018_03_01',
           '2018_04_01', '2018_05_01', '2018_06_01', '2018_07_01', '2018_08_01',
           '2018_09_01', '2018_10_01', '2018_11_01', '2018_12_01', '2019_01_01',
           '2019_02_01', '2019_03_01', '2019_04_01', '2019_05_01', '2019_06_01',
           '2019_07_01', '2019_08_01', '2019_09_01', '2019_10_01', '2019_11_01',
           '2019_12_01', '2020_01_01', '2020_02_01', '2020_03_01', '2020_04_01',
           '2020_05_01', '2020_06_01', '2020_07_01', '2020_08_01', '2020_09_01',
           '2020_10_01', '2020_11_01', '2020_12_01', '2021_01_01', '2021_02_01',
           '2021_03_01', '2021_04_01', '2021_05_01', '2021_06_01', '2021_07_01',
           '2021_08_01', '2021_09_01', '2021_10_01', '2021_11_01', '2021_12_01']
    
    
    kpi_value=pd.melt(kpi_value, id_vars=ids, value_vars=val,var_name='date',value_name='kpi_value')
    kpi_value['date']=pd.to_datetime(kpi_value.date,format='%Y_%m_%d').dt.date
    
    kpi_value.to_sql(name='kpi_value',con=new_integration,index=False,if_exists='append')
    return print('kpi_value stored in the database')


def processing_and_storing_milestones(milestones,new_integration):
    """
    Parameters
    ----------
    milestones : DataFrame
        Table containing Milestones Data
    new_integration : Object
        Connection to the DB
    
    Returns
    ----------
    None
    """
    
    milestones=milestones.drop(columns=['initiative_name'])
    milestones.to_sql(name='milestones',con=new_integration,index=False,if_exists='append')
    return print('milestones stored in the database')

def processing_and_storing_initiatives(initiatives,new_integration):
    """
    Parameters
    ----------
    initiatives : DataFrame
        Table containing initiatives Data
    new_integration : Object
        Connection to the DB
    
    Returns
    ----------
    initiatives : Data Frane 
    """
    
    init_cols=initiatives.columns.tolist()
    init_cols=[s.replace('_-','') for s in init_cols]
    init_cols=[s.replace('-','_') for s in init_cols]
    initiatives.columns=init_cols
    #Store it in the database 
    initiatives.to_sql(name='initiatives',con=new_integration,index=False,if_exists='append')
    print('initiatives stored in the database')
    return initiatives


def transforming_initiatives(initiatives,
                             impacts_description,
                             impacts_value,
                             impacts):
    """
    Transforming the initiatives and saving the history
    - we want to transform the data so that for every initiative,impact,purpose and saving type we have new calculation of impact values
    - for the P&L new value is the sum of the last 12 months and for Implemented is cumulative sum
    - we do the calculatons for every month beacause we need that for the reports

    
    Parameters
    ----------
    initiatives : DataFrame
        Table containing initiative data
    impacts_description : DataFrame
        Table containing impacts_description data
    impacts_value: DataFrame
        Table containing impact_value data
    impacts: DataFrame
        Table containing impacts data
        
    Returns
    ----------
    impacts_with_new: DataFrame
        Table containing impact_value data
    impacts: DataFrame
        Table containing impacts data
    """    
    initiatives=initiatives[['load_id','initiative_id','stage','weekly_status','report']]

    impacts=impacts_description.merge(impacts_value,how='inner',on=['id', 'load_id', 'impact_id','savings_type'])
    impacts=impacts.merge(initiatives,how='left',on=['load_id','initiative_id'])
    impacts.rename(columns={'impact_value':'wave_value'},inplace=True)
    
    impacts_with_new = impacts
    impacts_with_new.loc[impacts_with_new.wave_value.isna(),'wave_value']=0
    
    return impacts_with_new,impacts


def create_value_type_columns(df,flag):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """    
    '''
    flag = 0 pl_act
    glag = 1  pl_pln
    flag = 2 pl_frc
    '''
    
    for i in range(11):
        df.loc[:,'shift_{}'.format(i+1)]=df.groupby(['initiative_id','impact_id','purpose','savings_type']).wave_value.shift(periods=i+1)
        df.loc[df['shift_{}'.format(i+1)].isna(),'shift_{}'.format(i+1)]=0
    shift_columns=['wave_value','shift_1', 'shift_2', 'shift_3', 'shift_4',
    'shift_5', 'shift_6', 'shift_7', 'shift_8', 
    'shift_9', 'shift_10', 'shift_11']
    if flag == 0:
        df['dfual_value']=df[shift_columns].sum(axis=1)
        df['pl_plan_value'] = 0
        df['pl_forecast_value'] = 0
        
    if flag == 1:
        df['dfual_value'] = 0
        df['pl_plan_value']=df[shift_columns].sum(axis=1)
        df['pl_forecast_value'] = 0
    else:
        df['dfual_value'] = 0
        df['pl_plan_value']= 0
        df['pl_forecast_value'] = df[shift_columns].sum(axis=1)
        
    shift_columns.remove('wave_value')
    df.drop(columns=shift_columns,inplace=True)
    df['value_type']='12_months_sum' 
    return df 

def transofmring_impact_saving_implemented(impacts_with_new,impacts):
    """
    Transforming impacts
    - we create new column value where we save the calulations and
     make column value_type to know what calculation we did
    
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
     


    

    actual = impacts_with_new[(impacts_with_new.purpose == 'Actual')]
    forcast = impacts_with_new[(impacts_with_new.purpose == 'Forecast')]
    
    actual_forcast = actual.merge(forcast[['initiative_id','impact_id','savings_type','date','wave_value']],on = ['initiative_id','impact_id','savings_type','date'])
    actual_forcast['wave_value'] =actual_forcast.apply(lambda row: row['wave_value_x'] if row['wave_value_x'] >0 else row['wave_value_y'] , axis = 1)
    actual_forcast['purpose'] ='Actuals & Forecast'
    actual_forcast.drop(['wave_value_x','wave_value_y'],axis =1,inplace = True )
    
    plan = impacts_with_new[(impacts_with_new.purpose == 'Plan') ]
    impacts_with_new = pd.concat([plan,actual_forcast],ignore_index = True)

    impacts_with_new_selected=impacts_with_new[['initiative_id',
                                                'impact_id',
                                                'purpose',
                                                'savings_type',
                                                'date',
                                                'wave_value',
                                                'report']]

    saving = 'Implemented'
    imp=impacts_with_new_selected.query('savings_type==@saving') #.copy()

    imp_pln = imp.loc[(imp.purpose=='Plan'),]
    imp_frc = imp.loc[(imp.purpose=='Actuals & Forecast'),]

    imp.loc[:,'impact_plan_value']=imp_pln.groupby(['initiative_id','impact_id','purpose','savings_type']).wave_value.cumsum()
    imp.loc[:,'impact_forecast_value']=imp_frc.groupby(['initiative_id','impact_id','purpose','savings_type']).wave_value.cumsum()


    imp.loc[:,'pl_plan_value'] = 0
    imp.loc[:,'pl_forecast_value'] = 0
    
    imp['value_type'] = 'running_total'
    
    imp['impact_plan_value'].fillna(0, inplace=True)
    imp['impact_forecast_value'].fillna(0, inplace=True)
    
    
    saving='P&L'
#    impacts.loc[impacts.wave_value.isna(),'wave_value']=0
    pl_act = impacts_with_new_selected.query('savings_type==@saving')
    pl_act = pl_act.loc[(pl_act.purpose=='Actuals & Forecast'),]
    
    pl_act['impact_plan_value'] = 0
    pl_act['impact_forecast_value'] = 0

    pl_act = create_value_type_columns(pl_act,flag = 0)

    pl_pln = impacts_with_new_selected.query('savings_type==@saving')
    pl_pln = pl_pln.loc[(pl_pln.purpose=='Plan'),]
    
    pl_pln['impact_plan_value'] = 0
    pl_pln['impact_forecast_value'] = 0
     
    
    pl_pln = create_value_type_columns(pl_pln,flag = 1)
    
   
    
    pl = pl_act.append(pl_pln)
    
    impacts_all=pl.append(imp,ignore_index=True)
    
    impacts_out=impacts_with_new.merge(impacts_all,how='left',on=['initiative_id','impact_id',\
                                                        'purpose','savings_type', 'wave_value', 'date','report'])
    
    
       
    return impacts_out 
    
    
    
def creating_impact_simple(impacts_out):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
    
    impacts_simple = impacts_out.copy()
    impacts_simple['value'] = impacts_simple['impact_plan_value'] + impacts_simple['impact_forecast_value'] +impacts_simple['pl_plan_value'] + impacts_simple['pl_forecast_value']

    col = ['id', 'load_id', 'initiative_id', 'impact_id', 'workstream', 'impact_geography_country',
               'metric_metric_category', 'metric_metric', 'allocation_area_workstream', 'allocation_area_sub_workstream',
              'run_rate', 'savings_type', 'purpose', 'date', 'stage', 'weekly_status', 'wave_value', 'value', 'value_type','report']

    impacts_simple = impacts_simple[col]

    conditions = [
        (impacts_simple['workstream'] == 'G%26A'),
        (impacts_simple['workstream'] == 'R%26D')
    ]

    choices = ['G&A', 'R&D']

    impacts_simple['workstream'] = np.select(conditions, choices, default = impacts_simple['workstream'])

    conditions = [
        (impacts_simple['allocation_area_workstream'] == 'G%26A'),
        (impacts_simple['allocation_area_workstream'] == 'R%26D')
    ]

    choices = ['G&A', 'R&D']
    
    impacts_simple['allocation_area_workstream'] = np.select(conditions, choices, default = impacts_simple['allocation_area_workstream'])
    
    return impacts_simple


def closing_sessions(session):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
    
    session.close()
    print(str(session) + 'IS CLOSED!')
    

def read_xlsx_files(filename):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
    Initiatives_input = pd.read_excel(filename, 'Initiatives',skiprows=3)
    Milestones_input = pd.read_excel(filename, 'Milestones',skiprows=3)
    Impacts_input = pd.read_excel(filename, 'Impacts',skiprows=3)
    KPI_input = pd.read_excel(filename, 'KPI Details',skiprows=3)
    return Initiatives_input,Milestones_input,Impacts_input,KPI_input

def take_maximum_load_index(table,con):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
    table_load_id=pd.read_sql('{} {}'.format("SELECT max(load_id) FROM", table),con)

    table_id=pd.read_sql('{} {}'.format("SELECT max(id) FROM", table),con)
    return table_load_id.iloc[0,0],table_id.iloc[0,0]

def create_load_index(table,max_index,max_id):
    """
    Parameters
    ----------
    data : DataFrame
        Table containing Load_id as a column
    lid : int
        Load id
    
    Returns
    ----------
    new_data: DataFrame
    """ 
    cols = list(table.columns)
    table['load_id'] = max_index + 1 
    table['id'] = list(range(1,table.shape[0]+1))
    table = table[['id','load_id'] +cols]

    return table 


def create_new_columns_and_impace_2(impacts_simple):
    """
    This function is dealing with creating new columns CTO_stage and CTO_values for the inport data "impacts_simple". 
    The function is split in couple of parts: 
        1.1 The impact simple table is grouped by the following columns: 'load_id', 'initiative_id',  'workstream',
          'impact_geography_country', 'metric_metric_category', 'metric_metric',
           'allocation_area_workstream', 'allocation_area_sub_workstream',
          'savings_type', 'purpose', 'date', 'stage', 'weekly_status','value_type','report'
        1.2 smller_than_L3 temporaty table is created where we store all of the samples which are different than to "L4","L3", 
            "Submitted for L5 approval" and "Submitted for L4 approval"
        1.3 The rest of the data which don't belong to "smaller_than_L3"  is split in before merge and 
            after merge depening on the previous month taken by the month when this script is running. 
        1.4 Implemented and P&L values are calculated by the following logic:
            
             1.4.1  For Implemented savings_type 
                 - All of the instances which are before today have the following structure: 
                         "CTO_Stage" = 'L5' and "CTO_Value" the same as the P&L value for the same date and same ID. 
                         "CTO_Stage" =  "L3/L4"( depending on the previous level) and "CTO_Value"  = implemented_value - p&l_value . 
                         If the  implemented_value  < p&l_value we put " CTO_Value" = 0 
                 - All of the instances which are after today have the following structure: 
                         "CTO_Stage" = 'L5' and "CTO_Value"  = implemented_value - p&l_value(of today) 
                         "CTO_Stage" =  "L3/L4"( depending on the previous level) and "CTO_Value"  =  p&l_value(of today)   
                         If the  implemented_value  <  p&l_value(of today)    " CTO_Value" = 0 
            1.4.2. For P&L savings_type 
                - All of the instances which are before today have the following structure: 
                    "CTO_Stage" = 'L5' and "CTO_Value" the same as previous
                - All of the instances which are after today have the following structure: 
                    "CTO_Stage" = 'L5' and "CTO_Value"  = p&l_value - p&l_value(of today) 
                    "CTO_Stage" =  "L3/L4"( depending on the previous level) and "CTO_Value"  =  p&l_value(of today)   
                    If the   p&l_value    <  p&l_value(of today)    " CTO_Value" = 0 
    Parameters
    ----------
    impacts_simple : DataFrame
        Table containing impacts_simple data which is previosly stored in the DB 

    Returns
    ----------
    impact_simple_2: DataFrame
    """ 
    
    from datetime import date, timedelta
    import dateutil.relativedelta
    import datetime
    
    now = datetime.datetime.now()
    previous_month = datetime.datetime(now.year, now.month-1,1)
    
    list_columns_to_keep = ['load_id', 'initiative_id',  'workstream',
           'impact_geography_country', 'metric_metric_category', 'metric_metric',
           'allocation_area_workstream', 'allocation_area_sub_workstream',
          'savings_type', 'purpose', 'date', 'stage', 'weekly_status',
           'wave_value', 'value', 'value_type','report']
    
    impacts_simple[ 'impact_geography_country'] =     impacts_simple[ 'impact_geography_country'].fillna('-1')
    impacts_simple_grouped = impacts_simple[list_columns_to_keep].groupby(['load_id', 'initiative_id',  'workstream',
          'impact_geography_country', 'metric_metric_category', 'metric_metric',
           'allocation_area_workstream', 'allocation_area_sub_workstream',
          'savings_type', 'purpose', 'date', 'stage', 'weekly_status','value_type','report' ]  ).sum().reset_index()
    
    impacts_simple_grouped[ 'impact_geography_country'] =     impacts_simple_grouped[ 'impact_geography_country'].replace('-1',np.NaN)

    
    impacts_simple_grouped  = impacts_simple_grouped[impacts_simple_grouped.metric_metric_category != 'One-time impacts']
    
    impacts_simple = impacts_simple_grouped  
    
    smller_than_L3 = impacts_simple [(impacts_simple.stage != 'L4')& (impacts_simple.stage != 'L3')
    &(impacts_simple.stage != 'Submitted for L4 approval')& (impacts_simple.stage != 'Submitted for L5 approval') ]
    smller_than_L3['CTO_Value'] = smller_than_L3['value']
    smller_than_L3['CTO_Stage'] = smller_than_L3['stage']
    smller_than_L3 = smller_than_L3.rename(columns={'value': 'value_implemented'})
    
  
    
    before_today_implemented = impacts_simple[(pd.to_datetime(impacts_simple.date) <= previous_month) 
    & (impacts_simple.savings_type == 'Implemented')
    & ((impacts_simple.stage == 'L4')| (impacts_simple.stage == 'L3') |
            (impacts_simple.stage == 'Submitted for L5 approval')| (impacts_simple.stage == 'Submitted for L4 approval'))]
   
    
    after_today_implemented =   impacts_simple[(pd.to_datetime(impacts_simple.date) > previous_month) 
    & (impacts_simple.savings_type == 'Implemented')
    & ((impacts_simple.stage == 'L4')| (impacts_simple.stage == 'L3') |
            (impacts_simple.stage == 'Submitted for L5 approval')| (impacts_simple.stage == 'Submitted for L4 approval'))]
   
    
    today_pl = impacts_simple[(pd.to_datetime(impacts_simple.date) == previous_month) 
    & (impacts_simple.savings_type == 'P&L')
    & ((impacts_simple.stage == 'L4')| (impacts_simple.stage == 'L3') |
            (impacts_simple.stage == 'Submitted for L5 approval')| (impacts_simple.stage == 'Submitted for L4 approval'))]
   
   
    before_today_pl = impacts_simple[(pd.to_datetime(impacts_simple.date) <= previous_month)
    & (impacts_simple.savings_type == 'P&L')
    & ((impacts_simple.stage == 'L4')| (impacts_simple.stage == 'L3') |
            (impacts_simple.stage == 'Submitted for L5 approval')| (impacts_simple.stage == 'Submitted for L4 approval'))]
   
    
    after_today_pl=   impacts_simple[(pd.to_datetime(impacts_simple.date) > previous_month) 
    & (impacts_simple.savings_type == 'P&L')
    & ((impacts_simple.stage == 'L4')| (impacts_simple.stage == 'L3') |
            (impacts_simple.stage == 'Submitted for L5 approval')| (impacts_simple.stage == 'Submitted for L4 approval'))]
   
    
    ''' Implemented '''
    
    before_merge = before_today_implemented.merge(before_today_pl[['initiative_id','purpose','date','stage','value']],on = ['initiative_id','purpose','date','stage'])
    before_merge = before_merge.rename(columns={'value_x': 'value_implemented', 'value_y': 'value_pnl'})
    before_merge['CTO_Value'] = before_merge['value_implemented'] - before_merge['value_pnl']
    before_merge['CTO_Value'] =before_merge.apply(lambda row: 0 if row['CTO_Value'] <0 else row['CTO_Value'] , axis = 1)

   
    before_merge_1 = before_merge.drop('value_pnl',axis = 1)
    before_merge_1['CTO_Stage']=before_merge_1['stage']
    before_merge_2 = before_merge.drop('CTO_Value',axis = 1)
    before_merge_2 = before_merge_2.rename(columns={ 'value_pnl' : 'CTO_Value'})
    before_merge_2['CTO_Stage']='L5'
    before_merge = pd.concat([before_merge_1, before_merge_2], ignore_index=True)
    before_merge['savings_type'] = 'Implemented'
    
    
    
    after_merge = after_today_implemented.merge(today_pl[['initiative_id','purpose','stage','value']],on = ['initiative_id','purpose','stage'])
    after_merge = after_merge.rename(columns={'value_x': 'value_implemented', 'value_y': 'value_pnl'})
    after_merge['CTO_Value'] = after_merge['value_implemented'] - after_merge['value_pnl']
    after_merge['CTO_Value'] =after_merge.apply(lambda row: 0 if row['CTO_Value'] <0 else row['CTO_Value'] , axis = 1)


    after_merge_1 = after_merge.drop('value_pnl',axis = 1)
    after_merge_1['CTO_Stage']=after_merge_1['stage']
    after_merge_1 = after_merge_1.rename(columns={ 'date_x':'date'})
    after_merge_2 = after_merge.drop('CTO_Value',axis = 1)
    after_merge_2 = after_merge_2.rename(columns={ 'value_pnl' : 'CTO_Value','date_x':'date'})
    after_merge_2['CTO_Stage']= 'L5'
    after_merge = pd.concat([after_merge_1, after_merge_2], ignore_index=True)
    after_merge['savings_type'] = 'Implemented'
    
    before_today_pl['CTO_Stage'] = 'L5'
    before_today_pl['CTO_Value'] = before_today_pl['value']
    before_today_pl =  before_today_pl.rename(columns = {'value':'value_implemented'})
    
    ''' P&L'''
    
    after_merge_pl = after_today_pl.merge(today_pl[['initiative_id','purpose','stage','value']],on = ['initiative_id','purpose','stage'])
    after_merge_pl = after_merge_pl.rename(columns={'value_x': 'value_implemented', 'value_y': 'value_pnl'})
    after_merge_pl['CTO_Value'] = after_merge_pl['value_implemented'] - after_merge_pl['value_pnl']
    after_merge_pl['CTO_Value'] =after_merge_pl.apply(lambda row: 0 if row['CTO_Value'] <0 else row['CTO_Value'] , axis = 1)

    after_merge_1_pl = after_merge_pl.drop('value_pnl',axis = 1 )
    after_merge_1_pl = after_merge_1_pl.rename(columns={ 'date_x':'date'})
    after_merge_1_pl['CTO_Stage']=after_merge_1_pl['stage']
    after_merge_2_pl = after_merge_pl.drop('CTO_Value',axis = 1 )
    after_merge_2_pl = after_merge_2_pl.rename(columns={ 'value_pnl' : 'CTO_Value','date_x':'date'})
    after_merge_2_pl['CTO_Stage']='L5'
    after_merge_pl = pd.concat([after_merge_1_pl, after_merge_2_pl], ignore_index=True)
    after_merge_pl['savings_type'] = 'P&L'
    
    
    final = pd.concat([after_merge, after_merge_pl,before_merge,before_today_pl], ignore_index=True)

    impact_sample_2 = pd.concat([final,smller_than_L3],ignore_index = True)
    impact_sample_2 = impact_sample_2.rename(columns={ 'value_implemented' : 'value'})
    impact_sample_2[['value','CTO_Value']] = impact_sample_2[['value','CTO_Value']].round(2)
    

    return impact_sample_2

"""
STSADA PORJECT EXECUTION 

This script allows the user update the database from a new file "Wave data extract - Transforming STADA".
Steps to run the exe file: 
    1. Open the new Wave data extract - Transforming STADA.xlsm file and save it as an excel file 
    2. Put the new Wave data extract - Transforming STADA.xlsx file in the same repository as the reporting.exe 
    3. Go to the folder where reporting.exe program is and run it. 
    4. The new data should be stored in the impact_sample_2 table 
"""


import mysql.connector
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from io import StringIO
import xlrd
from variables import FILE_NAME_DIR


    
INITIATIVE_COLUMNS,MILESTONES_COLUMNS,IMPACTS_COLUMNS,KPI_COLUMNS = initialize_columns()

filename= FILE_NAME_DIR

engine = create_engine("mysql+mysqlconnector://m.durkan:1lqH8R3WzW4WFPsb@185.119.86.63/staging_layer")
stage = engine.connect()

engine = create_engine("mysql+mysqlconnector://m.durkan:1lqH8R3WzW4WFPsb@185.119.86.63/report_layer_test")
report = engine.connect()

engine = create_engine("mysql+mysqlconnector://m.durkan:1lqH8R3WzW4WFPsb@185.119.86.63/integration_layer_test")
new_integration = engine.connect()

print('READ EXCEL FILE ! ')
Initiatives_input,Milestones_input,Impacts_input,KPI_input = read_xlsx_files(filename)

print('TAKE MAXIMUM ID ')
Initiatives_max,initiatives_max_id = take_maximum_load_index('initiatives',stage)
Milestones_max,milestones_max_id = take_maximum_load_index('milestones',stage)
Impacts_max,imacts_max_id = take_maximum_load_index('impacts',stage)
KPI_max,kpi_max_id = take_maximum_load_index('kpidetails',stage)

print('GENERATE LOAD ID')
Initiatives_input = create_load_index(Initiatives_input,Initiatives_max,initiatives_max_id)
Milestones_input = create_load_index(Milestones_input,Milestones_max,milestones_max_id)
Impacts_input = create_load_index(Impacts_input,Impacts_max,imacts_max_id)
KPI_input = create_load_index(KPI_input,KPI_max,kpi_max_id)

print('TRUNCATE TABLES')
stage.execute( '''TRUNCATE TABLE initiatives''' )
stage.execute( '''TRUNCATE TABLE milestones''' )
stage.execute( '''TRUNCATE TABLE impacts''' )
stage.execute( '''TRUNCATE TABLE kpidetails''' )



print('STORE TABLES IN DATABASE STAGE')
Initiatives_input.columns = INITIATIVE_COLUMNS
stage.execute('''ALTER TABLE staging_layer.initiatives CONVERT TO CHARACTER SET utf8''')
Initiatives_input.to_sql(name = 'initiatives',con=stage,index = False,if_exists='append')

Milestones_input.columns = MILESTONES_COLUMNS
stage.execute('''ALTER TABLE staging_layer.milestones CONVERT TO CHARACTER SET utf8''')
Milestones_input.to_sql(name='milestones',con=stage,index=False,if_exists='append')

Impacts_input = Impacts_input.iloc[:,:69]
Impacts_input.columns= IMPACTS_COLUMNS
stage.execute('''ALTER TABLE staging_layer.impacts CONVERT TO CHARACTER SET utf8''')
Impacts_input.to_sql(name='impacts',con=stage,index=False,if_exists='replace')

KPI_input = KPI_input.iloc[:,:59]
KPI_input.columns = KPI_COLUMNS
stage.execute('''ALTER TABLE staging_layer.kpidetails CONVERT TO CHARACTER SET utf8''')
KPI_input.to_sql(name='kpidetails',con=stage,index=False,if_exists='replace')

print('LOADING TABLES')
impacts,kpi,milestones,initiatives = loading_tables(stage)

print('CHANGING THE IMPACT STATUS')
impacts = change_the_impact_status (impacts)

print('CHECK IF NEW TABLE IS LOADED')
check_new_table_loaded(new_integration,initiatives)

print('PRE-PROCESS IMPACT TABLE ')
impacts = pre_process_impact_columns(impacts)

print('SUBSETTING IMPACT TABLE! ')
impacts = subsetting_impacts(impacts)

print('CREATE IMPACT DESCRIPTION AND STORE' )
impacts_description = create_impact_description_and_store(impacts,new_integration)

print('CREATE AND STORE IMPACT VALUE')
impacts_value = create_and_store_impact_value(impacts,new_integration)

print('CREATE AND STORE KPI DESCRIPTION!')
create_and_store_kpi_descriptions(kpi,new_integration)

print('CREATE AND STORE KPI VALUE')
create_and_store_kpi_value(kpi,new_integration)    

print('PROCESSING AND STORING MILESTONE')
processing_and_storing_milestones(milestones,new_integration)

print('PROCESSING AND STORING INITIATIVES')
initiatives = processing_and_storing_initiatives(initiatives,new_integration)

print('TRANSFORMING INITIATIVES')
impacts_with_new,impacts = transforming_initiatives(initiatives,impacts_description,impacts_value,impacts)

print('TRANSFORMING IMPACT!')
impacts_out = transofmring_impact_saving_implemented(impacts_with_new,impacts)

print('CREATING IMPACT SIMPLE')
impacts_simple = creating_impact_simple(impacts_out)

print('STORE IMPACT SIMPLE')

stage.execute('''ALTER TABLE integration_layer_test.impact_simple CONVERT TO CHARACTER SET utf8''')
impacts_simple.to_sql(name='impact_simple',con=new_integration,index=False,if_exists='append')


engine = create_engine("mysql+mysqlconnector://m.durkan:1lqH8R3WzW4WFPsb@185.119.86.63/report_layer_test")
report = engine.connect()

stage.execute('''ALTER TABLE report_layer_test.impact_simple CONVERT TO CHARACTER SET utf8''')
impacts_simple.to_sql(name='impact_simple',con=report,index=False,if_exists='replace')  

print('CREATE IMPACT SAMPLE 2')
impact_sample_2 = create_new_columns_and_impace_2(impacts_simple)
print('STORE IMPACT SAMPLE 2')
impact_sample_2.to_sql(name='impact_simple_2',con=new_integration,index=False,if_exists='append')
impact_sample_2.to_sql(name='impact_simple_2',con=report,index=False,if_exists='replace') 

print('CLOSING SESSIONS....')
closing_sessions(report)
closing_sessions(new_integration)
closing_sessions(stage)


