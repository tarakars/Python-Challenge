

```python
#Importing Libraries
import pandas as pd
from sklearn import preprocessing
```


```python
#reading in the Json file as data frame by using pd.read_json funtion and printing the data by using head function.
purchase_data_df = pd.read_json('purchase_data.json')
purchase_data_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



#### Total Players


```python
no_of_players= len(purchase_data_df["SN"].unique()) #getting total players by using unique funtion and finding the lenght
no_of_players_df = pd.DataFrame({"Total Players":no_of_players},index = [0]) # creating a new Dataframe with total number of players
no_of_players_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



#### Purchase Analysis (Total)


```python
# Calculating the total purchase analysis
unique_items = len(purchase_data_df["Item ID"].unique()) # getting the len of unique items purchased
avg_purchase_price = purchase_data_df["Price"].mean() # getting the average price of items by using mean on price column
total_purchased = len(purchase_data_df) # getting lenght of the data frame so that we ger how many purchases are made
total_revenue = purchase_data_df["Price"].sum() # By doing the sum of the price column on the df we will get the total revenue

# creating a new dataframe with all the values you calculated with columns in the order we want
total_purhasing_analysis_df = pd.DataFrame({"No.Of unique items": unique_items,
                                           "Avergae Purchase Price": avg_purchase_price,
                                           "Total Purchases": total_purchased,
                                           "Total Revenue": total_revenue}, 
                                           columns = ["No.Of unique items","Total Purchases","Avergae Purchase Price","Total Revenue"],index = [0])
total_purhasing_analysis_df.style.format({"Total Purchases":"${:,.2f}","Avergae Purchase Price":"${:,.2f}","Total Revenue":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_1121c776_28c3_11e8_94de_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >No.Of unique items</th> 
        <th class="col_heading level0 col1" >Total Purchases</th> 
        <th class="col_heading level0 col2" >Avergae Purchase Price</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_1121c776_28c3_11e8_94de_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_1121c776_28c3_11e8_94de_8c85905c07d7row0_col0" class="data row0 col0" >183</td> 
        <td id="T_1121c776_28c3_11e8_94de_8c85905c07d7row0_col1" class="data row0 col1" >$780.00</td> 
        <td id="T_1121c776_28c3_11e8_94de_8c85905c07d7row0_col2" class="data row0 col2" >$2.93</td> 
        <td id="T_1121c776_28c3_11e8_94de_8c85905c07d7row0_col3" class="data row0 col3" >$2,286.33</td> 
    </tr></tbody> 
</table> 



#### Gender Demographics


```python
duplicates_removed_df = purchase_data_df.drop_duplicates(["SN"]) # removing duplicates from SN column, so that we can get how many male and females are in the data
male_count= len(duplicates_removed_df.loc[duplicates_removed_df["Gender"] == "Male"]) #filtering the data set by Male
female_count = len(duplicates_removed_df.loc[duplicates_removed_df["Gender"] == "Female"]) #filtering the data set by Female
others_count = len(duplicates_removed_df.loc[duplicates_removed_df["Gender"] == "Other / Non-Disclosed"])#filtering the data set by Others or disclosed
```


```python
#calculating the percentages of the male,female and other players
male_percentage = (male_count/len(purchase_data_df["SN"].unique()))*100
female_percentage = (female_count/len(purchase_data_df["SN"].unique()))*100
others_percentage = (others_count/len(purchase_data_df["SN"].unique()))*100
```


```python
# Creating a new data frame by using the values we got.
gender_demographics_df = pd.DataFrame({"Gender":["Male","Female","Others/Non-Disclosed"],
                                      "Total Count":[male_count,female_count,others_count],
                                      "Percentage":[male_percentage,female_percentage,others_percentage]},
                                     columns = ["Gender","Total Count","Percentage"])
gender_demographics_df.style.format({"Percentage":"{:,.2f}%"}) # formating the column to show the % symbol
```




<style  type="text/css" >
</style>  
<table id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Gender</th> 
        <th class="col_heading level0 col1" >Total Count</th> 
        <th class="col_heading level0 col2" >Percentage</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row0_col0" class="data row0 col0" >Male</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row0_col1" class="data row0 col1" >465</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row0_col2" class="data row0 col2" >81.15%</td> 
    </tr>    <tr> 
        <th id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row1_col0" class="data row1 col0" >Female</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row1_col1" class="data row1 col1" >100</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row1_col2" class="data row1 col2" >17.45%</td> 
    </tr>    <tr> 
        <th id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row2_col0" class="data row2 col0" >Others/Non-Disclosed</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row2_col1" class="data row2 col1" >8</td> 
        <td id="T_112a9888_28c3_11e8_a1cc_8c85905c07d7row2_col2" class="data row2 col2" >1.40%</td> 
    </tr></tbody> 
</table> 



#### Gender Purchase Analysis


```python
male_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Male"] #filtering all the data with gender male and pasing them to new Dataframe
male_purchase_count = len(male_df) #by using the lenght getting how many purchases Males made
male_average_price = male_df["Price"].mean() #by using mean calculating what is the avg price male spent
male_purchase_value = male_df["Price"].sum() #by using sum get the total revenue generated by male purchases.
```


```python
female_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Female"]#filtering all the data with gender female and pasing them to new Dataframe
female_purchase_count = len(female_df)#by using the lenght getting how many purchases females made
female_average_price = female_df["Price"].mean()#by using mean calculating what is the avg price female spent
female_purchase_value = female_df["Price"].sum()#by using sum get the total revenue generated by female purchases.
```


```python
# doing the same thing we did for male and female
others_df = purchase_data_df.loc[purchase_data_df["Gender"] == "Other / Non-Disclosed"]
others_purchase_count = len(others_df)
others_avergae_price = others_df["Price"].mean()
others_purchase_value = others_df["Price"].sum()
```


```python
#Creating a new data frame by the values we calculated to analyze
purchase_analysis_df = pd.DataFrame({"Gender":["Male","Female","Others/Non-Disclosed"],
                                    "Purchase_count":[male_purchase_count,female_purchase_count,others_purchase_count],
                                    "Average Purchase Price":[male_average_price,female_average_price,others_avergae_price],
                                    "Total purchase Value":[male_purchase_value,female_purchase_value,others_purchase_value]},
                                   columns = ["Gender","Purchase_count","Average Purchase Price","Total purchase Value"])
purchase_analysis_df.style.format({"Avergae Purchase Price":"${:,.2f}","Total purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_113198fe_28c3_11e8_83af_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Gender</th> 
        <th class="col_heading level0 col1" >Purchase_count</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Total purchase Value</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_113198fe_28c3_11e8_83af_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row0_col0" class="data row0 col0" >Male</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row0_col1" class="data row0 col1" >633</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row0_col2" class="data row0 col2" >2.95052</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row0_col3" class="data row0 col3" >$1,867.68</td> 
    </tr>    <tr> 
        <th id="T_113198fe_28c3_11e8_83af_8c85905c07d7level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row1_col0" class="data row1 col0" >Female</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row1_col1" class="data row1 col1" >136</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row1_col2" class="data row1 col2" >2.81551</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row1_col3" class="data row1 col3" >$382.91</td> 
    </tr>    <tr> 
        <th id="T_113198fe_28c3_11e8_83af_8c85905c07d7level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row2_col0" class="data row2 col0" >Others/Non-Disclosed</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row2_col1" class="data row2 col1" >11</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row2_col2" class="data row2 col2" >3.24909</td> 
        <td id="T_113198fe_28c3_11e8_83af_8c85905c07d7row2_col3" class="data row2 col3" >$35.74</td> 
    </tr></tbody> 
</table> 



#### Age Demographics


```python
# create bins for the different age ranges
bins = [0,9,14,19,purchase_data_df["Age"].max()] # creating bin for the max range
group_names = ["Less than 10","Between 10 to 15","Between 15 to 20", "Greater than 20"] # giving each group a nmae

#creating a new column called Age demographics and using cut to get the group name for differnt ages
purchase_data_df["Age Demographics"] = pd.cut(purchase_data_df["Age"],bins, labels = group_names)
purchase_data_df.style.format({"Price":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Age</th> 
        <th class="col_heading level0 col1" >Gender</th> 
        <th class="col_heading level0 col2" >Item ID</th> 
        <th class="col_heading level0 col3" >Item Name</th> 
        <th class="col_heading level0 col4" >Price</th> 
        <th class="col_heading level0 col5" >SN</th> 
        <th class="col_heading level0 col6" >Age Demographics</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col0" class="data row0 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col1" class="data row0 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col2" class="data row0 col2" >165</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col3" class="data row0 col3" >Bone Crushing Silver Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col4" class="data row0 col4" >$3.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col5" class="data row0 col5" >Aelalis34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row0_col6" class="data row0 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col0" class="data row1 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col1" class="data row1 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col2" class="data row1 col2" >119</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col3" class="data row1 col3" >Stormbringer, Dark Blade of Ending Misery</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col4" class="data row1 col4" >$2.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col5" class="data row1 col5" >Eolo46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row1_col6" class="data row1 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col0" class="data row2 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col1" class="data row2 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col2" class="data row2 col2" >174</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col3" class="data row2 col3" >Primitive Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col4" class="data row2 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col5" class="data row2 col5" >Assastnya25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row2_col6" class="data row2 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col0" class="data row3 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col1" class="data row3 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col2" class="data row3 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col3" class="data row3 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col4" class="data row3 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col5" class="data row3 col5" >Pheusrical25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row3_col6" class="data row3 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col0" class="data row4 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col1" class="data row4 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col2" class="data row4 col2" >63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col3" class="data row4 col3" >Stormfury Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col4" class="data row4 col4" >$1.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col5" class="data row4 col5" >Aela59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row4_col6" class="data row4 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row5" class="row_heading level0 row5" >5</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col0" class="data row5 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col1" class="data row5 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col2" class="data row5 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col3" class="data row5 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col4" class="data row5 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col5" class="data row5 col5" >Tanimnya91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row5_col6" class="data row5 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row6" class="row_heading level0 row6" >6</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col0" class="data row6 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col1" class="data row6 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col2" class="data row6 col2" >153</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col3" class="data row6 col3" >Mercenary Sabre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col4" class="data row6 col4" >$4.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col5" class="data row6 col5" >Undjaskla97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row6_col6" class="data row6 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row7" class="row_heading level0 row7" >7</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col0" class="data row7 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col1" class="data row7 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col2" class="data row7 col2" >169</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col3" class="data row7 col3" >Interrogator, Blood Blade of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col4" class="data row7 col4" >$3.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col5" class="data row7 col5" >Iathenudil29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row7_col6" class="data row7 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row8" class="row_heading level0 row8" >8</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col0" class="data row8 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col1" class="data row8 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col2" class="data row8 col2" >118</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col3" class="data row8 col3" >Ghost Reaver, Longsword of Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col4" class="data row8 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col5" class="data row8 col5" >Sondenasta63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row8_col6" class="data row8 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row9" class="row_heading level0 row9" >9</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col0" class="data row9 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col1" class="data row9 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col2" class="data row9 col2" >99</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col3" class="data row9 col3" >Expiration, Warscythe Of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col4" class="data row9 col4" >$4.53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col5" class="data row9 col5" >Hilaerin92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row9_col6" class="data row9 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row10" class="row_heading level0 row10" >10</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col0" class="data row10 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col1" class="data row10 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col2" class="data row10 col2" >57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col3" class="data row10 col3" >Despair, Favor of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col4" class="data row10 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col5" class="data row10 col5" >Chamosia29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row10_col6" class="data row10 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row11" class="row_heading level0 row11" >11</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col0" class="data row11 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col1" class="data row11 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col2" class="data row11 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col3" class="data row11 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col4" class="data row11 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col5" class="data row11 col5" >Sally64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row11_col6" class="data row11 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row12" class="row_heading level0 row12" >12</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col0" class="data row12 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col1" class="data row12 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col2" class="data row12 col2" >81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col3" class="data row12 col3" >Dreamkiss</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col4" class="data row12 col4" >$4.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col5" class="data row12 col5" >Iskossa88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row12_col6" class="data row12 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row13" class="row_heading level0 row13" >13</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col0" class="data row13 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col1" class="data row13 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col2" class="data row13 col2" >77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col3" class="data row13 col3" >Piety, Guardian of Riddles</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col4" class="data row13 col4" >$3.68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col5" class="data row13 col5" >Seorithstilis90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row13_col6" class="data row13 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row14" class="row_heading level0 row14" >14</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col0" class="data row14 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col1" class="data row14 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col2" class="data row14 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col3" class="data row14 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col4" class="data row14 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col5" class="data row14 col5" >Sundast29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row14_col6" class="data row14 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row15" class="row_heading level0 row15" >15</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col0" class="data row15 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col1" class="data row15 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col2" class="data row15 col2" >96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col3" class="data row15 col3" >Blood-Forged Skeletal Spine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col4" class="data row15 col4" >$4.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col5" class="data row15 col5" >Haellysu29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row15_col6" class="data row15 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row16" class="row_heading level0 row16" >16</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col0" class="data row16 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col1" class="data row16 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col2" class="data row16 col2" >123</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col3" class="data row16 col3" >Twilight's Carver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col4" class="data row16 col4" >$1.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col5" class="data row16 col5" >Sundista85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row16_col6" class="data row16 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row17" class="row_heading level0 row17" >17</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col0" class="data row17 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col1" class="data row17 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col2" class="data row17 col2" >59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col3" class="data row17 col3" >Lightning, Etcher of the King</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col4" class="data row17 col4" >$1.65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col5" class="data row17 col5" >Aenarap34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row17_col6" class="data row17 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row18" class="row_heading level0 row18" >18</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col0" class="data row18 col0" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col1" class="data row18 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col2" class="data row18 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col3" class="data row18 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col4" class="data row18 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col5" class="data row18 col5" >Iskista88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row18_col6" class="data row18 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row19" class="row_heading level0 row19" >19</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col0" class="data row19 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col1" class="data row19 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col2" class="data row19 col2" >177</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col3" class="data row19 col3" >Winterthorn, Defender of Shifting Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col4" class="data row19 col4" >$4.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col5" class="data row19 col5" >Assossa43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row19_col6" class="data row19 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row20" class="row_heading level0 row20" >20</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col0" class="data row20 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col1" class="data row20 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col2" class="data row20 col2" >78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col3" class="data row20 col3" >Glimmer, Ender of the Moon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col4" class="data row20 col4" >$2.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col5" class="data row20 col5" >Irith83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row20_col6" class="data row20 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row21" class="row_heading level0 row21" >21</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col0" class="data row21 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col1" class="data row21 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col2" class="data row21 col2" >3</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col3" class="data row21 col3" >Phantomlight</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col4" class="data row21 col4" >$1.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col5" class="data row21 col5" >Iaralrgue74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row21_col6" class="data row21 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row22" class="row_heading level0 row22" >22</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col0" class="data row22 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col1" class="data row22 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col2" class="data row22 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col3" class="data row22 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col4" class="data row22 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col5" class="data row22 col5" >Deural48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row22_col6" class="data row22 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row23" class="row_heading level0 row23" >23</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col0" class="data row23 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col1" class="data row23 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col2" class="data row23 col2" >183</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col3" class="data row23 col3" >Dragon's Greatsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col4" class="data row23 col4" >$2.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col5" class="data row23 col5" >Chanosia65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row23_col6" class="data row23 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row24" class="row_heading level0 row24" >24</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col0" class="data row24 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col1" class="data row24 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col2" class="data row24 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col3" class="data row24 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col4" class="data row24 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col5" class="data row24 col5" >Qarwen67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row24_col6" class="data row24 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row25" class="row_heading level0 row25" >25</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col0" class="data row25 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col1" class="data row25 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col2" class="data row25 col2" >63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col3" class="data row25 col3" >Stormfury Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col4" class="data row25 col4" >$1.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col5" class="data row25 col5" >Idai61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row25_col6" class="data row25 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row26" class="row_heading level0 row26" >26</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col0" class="data row26 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col1" class="data row26 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col2" class="data row26 col2" >132</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col3" class="data row26 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col4" class="data row26 col4" >$3.90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col5" class="data row26 col5" >Aerithllora36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row26_col6" class="data row26 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row27" class="row_heading level0 row27" >27</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col0" class="data row27 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col1" class="data row27 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col2" class="data row27 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col3" class="data row27 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col4" class="data row27 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col5" class="data row27 col5" >Assastnya25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row27_col6" class="data row27 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row28" class="row_heading level0 row28" >28</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col0" class="data row28 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col1" class="data row28 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col2" class="data row28 col2" >49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col3" class="data row28 col3" >The Oculus, Token of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col4" class="data row28 col4" >$4.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col5" class="data row28 col5" >Ilariarin45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row28_col6" class="data row28 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row29" class="row_heading level0 row29" >29</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col0" class="data row29 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col1" class="data row29 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col2" class="data row29 col2" >45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col3" class="data row29 col3" >Glinting Glass Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col4" class="data row29 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col5" class="data row29 col5" >Phaedai25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row29_col6" class="data row29 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row30" class="row_heading level0 row30" >30</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col0" class="data row30 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col1" class="data row30 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col2" class="data row30 col2" >155</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col3" class="data row30 col3" >War-Forged Gold Deflector</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col4" class="data row30 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col5" class="data row30 col5" >Eulaeria40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row30_col6" class="data row30 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row31" class="row_heading level0 row31" >31</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col0" class="data row31 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col1" class="data row31 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col2" class="data row31 col2" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col3" class="data row31 col3" >Shadow Strike, Glory of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col4" class="data row31 col4" >$1.93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col5" class="data row31 col5" >Iarilis73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row31_col6" class="data row31 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row32" class="row_heading level0 row32" >32</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col0" class="data row32 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col1" class="data row32 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col2" class="data row32 col2" >48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col3" class="data row32 col3" >Rage, Legacy of the Lone Victor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col4" class="data row32 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col5" class="data row32 col5" >Malunil62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row32_col6" class="data row32 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row33" class="row_heading level0 row33" >33</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col0" class="data row33 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col1" class="data row33 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col2" class="data row33 col2" >90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col3" class="data row33 col3" >Betrayer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col4" class="data row33 col4" >$1.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col5" class="data row33 col5" >Iskimnya76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row33_col6" class="data row33 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row34" class="row_heading level0 row34" >34</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col0" class="data row34 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col1" class="data row34 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col2" class="data row34 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col3" class="data row34 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col4" class="data row34 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col5" class="data row34 col5" >Yararmol43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row34_col6" class="data row34 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row35" class="row_heading level0 row35" >35</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col0" class="data row35 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col1" class="data row35 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col2" class="data row35 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col3" class="data row35 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col4" class="data row35 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col5" class="data row35 col5" >Aisur51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row35_col6" class="data row35 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row36" class="row_heading level0 row36" >36</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col0" class="data row36 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col1" class="data row36 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col2" class="data row36 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col3" class="data row36 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col4" class="data row36 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col5" class="data row36 col5" >Undare39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row36_col6" class="data row36 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row37" class="row_heading level0 row37" >37</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col0" class="data row37 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col1" class="data row37 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col2" class="data row37 col2" >171</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col3" class="data row37 col3" >Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col4" class="data row37 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col5" class="data row37 col5" >Sondossa91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row37_col6" class="data row37 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row38" class="row_heading level0 row38" >38</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col0" class="data row38 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col1" class="data row38 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col2" class="data row38 col2" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col3" class="data row38 col3" >Hero Cane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col4" class="data row38 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col5" class="data row38 col5" >Chamjasknya65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row38_col6" class="data row38 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row39" class="row_heading level0 row39" >39</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col0" class="data row39 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col1" class="data row39 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col2" class="data row39 col2" >63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col3" class="data row39 col3" >Stormfury Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col4" class="data row39 col4" >$1.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col5" class="data row39 col5" >Lassilsa63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row39_col6" class="data row39 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row40" class="row_heading level0 row40" >40</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col0" class="data row40 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col1" class="data row40 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col2" class="data row40 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col3" class="data row40 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col4" class="data row40 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col5" class="data row40 col5" >Tyisur83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row40_col6" class="data row40 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row41" class="row_heading level0 row41" >41</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col0" class="data row41 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col1" class="data row41 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col2" class="data row41 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col3" class="data row41 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col4" class="data row41 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col5" class="data row41 col5" >Aeral43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row41_col6" class="data row41 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row42" class="row_heading level0 row42" >42</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col0" class="data row42 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col1" class="data row42 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col2" class="data row42 col2" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col3" class="data row42 col3" >Hero Cane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col4" class="data row42 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col5" class="data row42 col5" >Lassadarsda57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row42_col6" class="data row42 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row43" class="row_heading level0 row43" >43</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col0" class="data row43 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col1" class="data row43 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col2" class="data row43 col2" >68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col3" class="data row43 col3" >Storm-Weaver, Slayer of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col4" class="data row43 col4" >$2.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col5" class="data row43 col5" >Alaephos75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row43_col6" class="data row43 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row44" class="row_heading level0 row44" >44</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col0" class="data row44 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col1" class="data row44 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col2" class="data row44 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col3" class="data row44 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col4" class="data row44 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col5" class="data row44 col5" >Frichjask31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row44_col6" class="data row44 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row45" class="row_heading level0 row45" >45</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col0" class="data row45 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col1" class="data row45 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col2" class="data row45 col2" >120</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col3" class="data row45 col3" >Agatha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col4" class="data row45 col4" >$1.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col5" class="data row45 col5" >Eusur90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row45_col6" class="data row45 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row46" class="row_heading level0 row46" >46</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col0" class="data row46 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col1" class="data row46 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col2" class="data row46 col2" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col3" class="data row46 col3" >Lazarus, Terror of the Earth</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col4" class="data row46 col4" >$3.47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col5" class="data row46 col5" >Palatyon26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row46_col6" class="data row46 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row47" class="row_heading level0 row47" >47</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col0" class="data row47 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col1" class="data row47 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col2" class="data row47 col2" >141</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col3" class="data row47 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col4" class="data row47 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col5" class="data row47 col5" >Saellyra72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row47_col6" class="data row47 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row48" class="row_heading level0 row48" >48</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col0" class="data row48 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col1" class="data row48 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col2" class="data row48 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col3" class="data row48 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col4" class="data row48 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col5" class="data row48 col5" >Ililsa62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row48_col6" class="data row48 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row49" class="row_heading level0 row49" >49</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col0" class="data row49 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col1" class="data row49 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col2" class="data row49 col2" >151</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col3" class="data row49 col3" >Severance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col4" class="data row49 col4" >$1.85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col5" class="data row49 col5" >Eosur70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row49_col6" class="data row49 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row50" class="row_heading level0 row50" >50</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col0" class="data row50 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col1" class="data row50 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col2" class="data row50 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col3" class="data row50 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col4" class="data row50 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col5" class="data row50 col5" >Saistyphos30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row50_col6" class="data row50 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row51" class="row_heading level0 row51" >51</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col0" class="data row51 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col1" class="data row51 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col2" class="data row51 col2" >169</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col3" class="data row51 col3" >Interrogator, Blood Blade of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col4" class="data row51 col4" >$3.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col5" class="data row51 col5" >Reula64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row51_col6" class="data row51 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row52" class="row_heading level0 row52" >52</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col0" class="data row52 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col1" class="data row52 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col2" class="data row52 col2" >165</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col3" class="data row52 col3" >Bone Crushing Silver Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col4" class="data row52 col4" >$3.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col5" class="data row52 col5" >Chanirrala39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row52_col6" class="data row52 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row53" class="row_heading level0 row53" >53</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col0" class="data row53 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col1" class="data row53 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col2" class="data row53 col2" >51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col3" class="data row53 col3" >Endbringer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col4" class="data row53 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col5" class="data row53 col5" >Chadanto83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row53_col6" class="data row53 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row54" class="row_heading level0 row54" >54</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col0" class="data row54 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col1" class="data row54 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col2" class="data row54 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col3" class="data row54 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col4" class="data row54 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col5" class="data row54 col5" >Minduli80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row54_col6" class="data row54 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row55" class="row_heading level0 row55" >55</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col0" class="data row55 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col1" class="data row55 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col2" class="data row55 col2" >140</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col3" class="data row55 col3" >Striker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col4" class="data row55 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col5" class="data row55 col5" >Heunadil74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row55_col6" class="data row55 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row56" class="row_heading level0 row56" >56</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col0" class="data row56 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col1" class="data row56 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col2" class="data row56 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col3" class="data row56 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col4" class="data row56 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col5" class="data row56 col5" >Marilsasya33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row56_col6" class="data row56 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row57" class="row_heading level0 row57" >57</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col0" class="data row57 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col1" class="data row57 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col2" class="data row57 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col3" class="data row57 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col4" class="data row57 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col5" class="data row57 col5" >Alallo58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row57_col6" class="data row57 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row58" class="row_heading level0 row58" >58</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col0" class="data row58 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col1" class="data row58 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col2" class="data row58 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col3" class="data row58 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col4" class="data row58 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col5" class="data row58 col5" >Tyaeristi78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row58_col6" class="data row58 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row59" class="row_heading level0 row59" >59</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col0" class="data row59 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col1" class="data row59 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col2" class="data row59 col2" >2</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col3" class="data row59 col3" >Verdict</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col4" class="data row59 col4" >$3.40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col5" class="data row59 col5" >Ila44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row59_col6" class="data row59 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row60" class="row_heading level0 row60" >60</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col0" class="data row60 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col1" class="data row60 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col2" class="data row60 col2" >86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col3" class="data row60 col3" >Stormfury Lantern</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col4" class="data row60 col4" >$1.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col5" class="data row60 col5" >Iskossaya95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row60_col6" class="data row60 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row61" class="row_heading level0 row61" >61</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col0" class="data row61 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col1" class="data row61 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col2" class="data row61 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col3" class="data row61 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col4" class="data row61 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col5" class="data row61 col5" >Rinallorap73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row61_col6" class="data row61 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row62" class="row_heading level0 row62" >62</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col0" class="data row62 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col1" class="data row62 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col2" class="data row62 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col3" class="data row62 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col4" class="data row62 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col5" class="data row62 col5" >Aeri84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row62_col6" class="data row62 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row63" class="row_heading level0 row63" >63</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col0" class="data row63 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col1" class="data row63 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col2" class="data row63 col2" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col3" class="data row63 col3" >Flux, Destroyer of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col4" class="data row63 col4" >$3.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col5" class="data row63 col5" >Ryanara76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row63_col6" class="data row63 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row64" class="row_heading level0 row64" >64</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col0" class="data row64 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col1" class="data row64 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col2" class="data row64 col2" >160</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col3" class="data row64 col3" >Azurewrath</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col4" class="data row64 col4" >$2.22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col5" class="data row64 col5" >Syally44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row64_col6" class="data row64 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row65" class="row_heading level0 row65" >65</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col0" class="data row65 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col1" class="data row65 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col2" class="data row65 col2" >134</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col3" class="data row65 col3" >Undead Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col4" class="data row65 col4" >$4.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col5" class="data row65 col5" >Shaidanu32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row65_col6" class="data row65 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row66" class="row_heading level0 row66" >66</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col0" class="data row66 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col1" class="data row66 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col2" class="data row66 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col3" class="data row66 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col4" class="data row66 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col5" class="data row66 col5" >Syasriria69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row66_col6" class="data row66 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row67" class="row_heading level0 row67" >67</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col0" class="data row67 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col1" class="data row67 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col2" class="data row67 col2" >83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col3" class="data row67 col3" >Lifebender</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col4" class="data row67 col4" >$3.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col5" class="data row67 col5" >Lisiriya82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row67_col6" class="data row67 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row68" class="row_heading level0 row68" >68</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col0" class="data row68 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col1" class="data row68 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col2" class="data row68 col2" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col3" class="data row68 col3" >The Void, Vengeance of Dark Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col4" class="data row68 col4" >$2.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col5" class="data row68 col5" >Qarwen67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row68_col6" class="data row68 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row69" class="row_heading level0 row69" >69</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col0" class="data row69 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col1" class="data row69 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col2" class="data row69 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col3" class="data row69 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col4" class="data row69 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col5" class="data row69 col5" >Iskosia51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row69_col6" class="data row69 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row70" class="row_heading level0 row70" >70</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col0" class="data row70 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col1" class="data row70 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col2" class="data row70 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col3" class="data row70 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col4" class="data row70 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col5" class="data row70 col5" >Eosurdru76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row70_col6" class="data row70 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row71" class="row_heading level0 row71" >71</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col0" class="data row71 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col1" class="data row71 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col2" class="data row71 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col3" class="data row71 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col4" class="data row71 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col5" class="data row71 col5" >Lassimla92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row71_col6" class="data row71 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row72" class="row_heading level0 row72" >72</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col0" class="data row72 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col1" class="data row72 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col2" class="data row72 col2" >110</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col3" class="data row72 col3" >Suspension</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col4" class="data row72 col4" >$2.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col5" class="data row72 col5" >Tauldilsa43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row72_col6" class="data row72 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row73" class="row_heading level0 row73" >73</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col0" class="data row73 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col1" class="data row73 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col2" class="data row73 col2" >122</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col3" class="data row73 col3" >Unending Tyranny</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col4" class="data row73 col4" >$1.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col5" class="data row73 col5" >Erudrion71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row73_col6" class="data row73 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row74" class="row_heading level0 row74" >74</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col0" class="data row74 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col1" class="data row74 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col2" class="data row74 col2" >54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col3" class="data row74 col3" >Eternal Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col4" class="data row74 col4" >$3.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col5" class="data row74 col5" >Chanjaskan37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row74_col6" class="data row74 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row75" class="row_heading level0 row75" >75</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col0" class="data row75 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col1" class="data row75 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col2" class="data row75 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col3" class="data row75 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col4" class="data row75 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col5" class="data row75 col5" >Sondastan54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row75_col6" class="data row75 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row76" class="row_heading level0 row76" >76</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col0" class="data row76 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col1" class="data row76 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col2" class="data row76 col2" >105</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col3" class="data row76 col3" >Hailstorm Shadowsteel Scythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col4" class="data row76 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col5" class="data row76 col5" >Strithenu87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row76_col6" class="data row76 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row77" class="row_heading level0 row77" >77</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col0" class="data row77 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col1" class="data row77 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col2" class="data row77 col2" >87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col3" class="data row77 col3" >Deluge, Edge of the West</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col4" class="data row77 col4" >$2.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col5" class="data row77 col5" >Chanastsda67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row77_col6" class="data row77 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row78" class="row_heading level0 row78" >78</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col0" class="data row78 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col1" class="data row78 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col2" class="data row78 col2" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col3" class="data row78 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col4" class="data row78 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col5" class="data row78 col5" >Baelollodeu94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row78_col6" class="data row78 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row79" class="row_heading level0 row79" >79</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col0" class="data row79 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col1" class="data row79 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col2" class="data row79 col2" >144</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col3" class="data row79 col3" >Blood Infused Guardian</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col4" class="data row79 col4" >$2.86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col5" class="data row79 col5" >Undirrala66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row79_col6" class="data row79 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row80" class="row_heading level0 row80" >80</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col0" class="data row80 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col1" class="data row80 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col2" class="data row80 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col3" class="data row80 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col4" class="data row80 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col5" class="data row80 col5" >Chanosseya79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row80_col6" class="data row80 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row81" class="row_heading level0 row81" >81</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col0" class="data row81 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col1" class="data row81 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col2" class="data row81 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col3" class="data row81 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col4" class="data row81 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col5" class="data row81 col5" >Yaristi64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row81_col6" class="data row81 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row82" class="row_heading level0 row82" >82</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col0" class="data row82 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col1" class="data row82 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col2" class="data row82 col2" >46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col3" class="data row82 col3" >Hopeless Ebon Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col4" class="data row82 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col5" class="data row82 col5" >Airi27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row82_col6" class="data row82 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row83" class="row_heading level0 row83" >83</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col0" class="data row83 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col1" class="data row83 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col2" class="data row83 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col3" class="data row83 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col4" class="data row83 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col5" class="data row83 col5" >Frichaststa61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row83_col6" class="data row83 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row84" class="row_heading level0 row84" >84</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col0" class="data row84 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col1" class="data row84 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col2" class="data row84 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col3" class="data row84 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col4" class="data row84 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col5" class="data row84 col5" >Raysistast71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row84_col6" class="data row84 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row85" class="row_heading level0 row85" >85</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col0" class="data row85 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col1" class="data row85 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col2" class="data row85 col2" >150</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col3" class="data row85 col3" >Deathraze</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col4" class="data row85 col4" >$4.54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col5" class="data row85 col5" >Ithergue48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row85_col6" class="data row85 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row86" class="row_heading level0 row86" >86</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col0" class="data row86 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col1" class="data row86 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col2" class="data row86 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col3" class="data row86 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col4" class="data row86 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col5" class="data row86 col5" >Chanastst38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row86_col6" class="data row86 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row87" class="row_heading level0 row87" >87</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col0" class="data row87 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col1" class="data row87 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col2" class="data row87 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col3" class="data row87 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col4" class="data row87 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col5" class="data row87 col5" >Sundosiasta28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row87_col6" class="data row87 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row88" class="row_heading level0 row88" >88</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col0" class="data row88 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col1" class="data row88 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col2" class="data row88 col2" >132</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col3" class="data row88 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col4" class="data row88 col4" >$3.90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col5" class="data row88 col5" >Undotesta33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row88_col6" class="data row88 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row89" class="row_heading level0 row89" >89</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col0" class="data row89 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col1" class="data row89 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col2" class="data row89 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col3" class="data row89 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col4" class="data row89 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col5" class="data row89 col5" >Tyiaduenuru55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row89_col6" class="data row89 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row90" class="row_heading level0 row90" >90</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col0" class="data row90 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col1" class="data row90 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col2" class="data row90 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col3" class="data row90 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col4" class="data row90 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col5" class="data row90 col5" >Iskjaskst81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row90_col6" class="data row90 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row91" class="row_heading level0 row91" >91</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col0" class="data row91 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col1" class="data row91 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col2" class="data row91 col2" >167</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col3" class="data row91 col3" >Malice, Legacy of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col4" class="data row91 col4" >$2.38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col5" class="data row91 col5" >Iskjaskan81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row91_col6" class="data row91 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row92" class="row_heading level0 row92" >92</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col0" class="data row92 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col1" class="data row92 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col2" class="data row92 col2" >181</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col3" class="data row92 col3" >Reaper's Toll</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col4" class="data row92 col4" >$4.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col5" class="data row92 col5" >Frichim27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row92_col6" class="data row92 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row93" class="row_heading level0 row93" >93</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col0" class="data row93 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col1" class="data row93 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col2" class="data row93 col2" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col3" class="data row93 col3" >Netherbane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col4" class="data row93 col4" >$1.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col5" class="data row93 col5" >Hailaphos89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row93_col6" class="data row93 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row94" class="row_heading level0 row94" >94</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col0" class="data row94 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col1" class="data row94 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col2" class="data row94 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col3" class="data row94 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col4" class="data row94 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col5" class="data row94 col5" >Seorithstilis90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row94_col6" class="data row94 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row95" class="row_heading level0 row95" >95</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col0" class="data row95 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col1" class="data row95 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col2" class="data row95 col2" >111</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col3" class="data row95 col3" >Misery's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col4" class="data row95 col4" >$2.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col5" class="data row95 col5" >Jiskjask80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row95_col6" class="data row95 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row96" class="row_heading level0 row96" >96</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col0" class="data row96 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col1" class="data row96 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col2" class="data row96 col2" >54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col3" class="data row96 col3" >Eternal Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col4" class="data row96 col4" >$3.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col5" class="data row96 col5" >Yasurra52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row96_col6" class="data row96 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row97" class="row_heading level0 row97" >97</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col0" class="data row97 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col1" class="data row97 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col2" class="data row97 col2" >49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col3" class="data row97 col3" >The Oculus, Token of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col4" class="data row97 col4" >$4.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col5" class="data row97 col5" >Assassasta79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row97_col6" class="data row97 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row98" class="row_heading level0 row98" >98</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col0" class="data row98 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col1" class="data row98 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col2" class="data row98 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col3" class="data row98 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col4" class="data row98 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col5" class="data row98 col5" >Lamyon68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row98_col6" class="data row98 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row99" class="row_heading level0 row99" >99</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col0" class="data row99 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col1" class="data row99 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col2" class="data row99 col2" >110</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col3" class="data row99 col3" >Suspension</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col4" class="data row99 col4" >$2.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col5" class="data row99 col5" >Alo67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row99_col6" class="data row99 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row100" class="row_heading level0 row100" >100</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col0" class="data row100 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col1" class="data row100 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col2" class="data row100 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col3" class="data row100 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col4" class="data row100 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col5" class="data row100 col5" >Farenon57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row100_col6" class="data row100 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row101" class="row_heading level0 row101" >101</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col0" class="data row101 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col1" class="data row101 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col2" class="data row101 col2" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col3" class="data row101 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col4" class="data row101 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col5" class="data row101 col5" >Assistasda90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row101_col6" class="data row101 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row102" class="row_heading level0 row102" >102</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col0" class="data row102 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col1" class="data row102 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col2" class="data row102 col2" >51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col3" class="data row102 col3" >Endbringer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col4" class="data row102 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col5" class="data row102 col5" >Frichaya88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row102_col6" class="data row102 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row103" class="row_heading level0 row103" >103</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col0" class="data row103 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col1" class="data row103 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col2" class="data row103 col2" >139</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col3" class="data row103 col3" >Mercy, Katana of Dismay</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col4" class="data row103 col4" >$4.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col5" class="data row103 col5" >Marassanya92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row103_col6" class="data row103 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row104" class="row_heading level0 row104" >104</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col0" class="data row104 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col1" class="data row104 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col2" class="data row104 col2" >173</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col3" class="data row104 col3" >Stormfury Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col4" class="data row104 col4" >$4.83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col5" class="data row104 col5" >Iskista96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row104_col6" class="data row104 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row105" class="row_heading level0 row105" >105</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col0" class="data row105 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col1" class="data row105 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col2" class="data row105 col2" >55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col3" class="data row105 col3" >Vindictive Glass Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col4" class="data row105 col4" >$4.26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col5" class="data row105 col5" >Mindirra92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row105_col6" class="data row105 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row106" class="row_heading level0 row106" >106</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col0" class="data row106 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col1" class="data row106 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col2" class="data row106 col2" >174</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col3" class="data row106 col3" >Primitive Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col4" class="data row106 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col5" class="data row106 col5" >Chadossa56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row106_col6" class="data row106 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row107" class="row_heading level0 row107" >107</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col0" class="data row107 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col1" class="data row107 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col2" class="data row107 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col3" class="data row107 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col4" class="data row107 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col5" class="data row107 col5" >Undirrala66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row107_col6" class="data row107 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row108" class="row_heading level0 row108" >108</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col0" class="data row108 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col1" class="data row108 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col2" class="data row108 col2" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col3" class="data row108 col3" >Heartless Bone Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col4" class="data row108 col4" >$2.63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col5" class="data row108 col5" >Eoda93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row108_col6" class="data row108 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row109" class="row_heading level0 row109" >109</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col0" class="data row109 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col1" class="data row109 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col2" class="data row109 col2" >42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col3" class="data row109 col3" >The Decapitator</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col4" class="data row109 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col5" class="data row109 col5" >Lassast89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row109_col6" class="data row109 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row110" class="row_heading level0 row110" >110</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col0" class="data row110 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col1" class="data row110 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col2" class="data row110 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col3" class="data row110 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col4" class="data row110 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col5" class="data row110 col5" >Philodil43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row110_col6" class="data row110 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row111" class="row_heading level0 row111" >111</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col0" class="data row111 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col1" class="data row111 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col2" class="data row111 col2" >160</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col3" class="data row111 col3" >Azurewrath</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col4" class="data row111 col4" >$2.22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col5" class="data row111 col5" >Tyirithnu40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row111_col6" class="data row111 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row112" class="row_heading level0 row112" >112</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col0" class="data row112 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col1" class="data row112 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col2" class="data row112 col2" >57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col3" class="data row112 col3" >Despair, Favor of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col4" class="data row112 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col5" class="data row112 col5" >Haerith37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row112_col6" class="data row112 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row113" class="row_heading level0 row113" >113</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col0" class="data row113 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col1" class="data row113 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col2" class="data row113 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col3" class="data row113 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col4" class="data row113 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col5" class="data row113 col5" >Jeyciman68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row113_col6" class="data row113 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row114" class="row_heading level0 row114" >114</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col0" class="data row114 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col1" class="data row114 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col2" class="data row114 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col3" class="data row114 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col4" class="data row114 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col5" class="data row114 col5" >Chamirraya83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row114_col6" class="data row114 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row115" class="row_heading level0 row115" >115</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col0" class="data row115 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col1" class="data row115 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col2" class="data row115 col2" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col3" class="data row115 col3" >Thorn, Conqueror of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col4" class="data row115 col4" >$2.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col5" class="data row115 col5" >Yasur85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row115_col6" class="data row115 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row116" class="row_heading level0 row116" >116</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col0" class="data row116 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col1" class="data row116 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col2" class="data row116 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col3" class="data row116 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col4" class="data row116 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col5" class="data row116 col5" >Koikirra25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row116_col6" class="data row116 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row117" class="row_heading level0 row117" >117</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col0" class="data row117 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col1" class="data row117 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col2" class="data row117 col2" >160</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col3" class="data row117 col3" >Azurewrath</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col4" class="data row117 col4" >$2.22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col5" class="data row117 col5" >Qarwen67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row117_col6" class="data row117 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row118" class="row_heading level0 row118" >118</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col0" class="data row118 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col1" class="data row118 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col2" class="data row118 col2" >46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col3" class="data row118 col3" >Hopeless Ebon Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col4" class="data row118 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col5" class="data row118 col5" >Quarunarn52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row118_col6" class="data row118 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row119" class="row_heading level0 row119" >119</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col0" class="data row119 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col1" class="data row119 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col2" class="data row119 col2" >180</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col3" class="data row119 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col4" class="data row119 col4" >$2.78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col5" class="data row119 col5" >Yasur35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row119_col6" class="data row119 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row120" class="row_heading level0 row120" >120</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col0" class="data row120 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col1" class="data row120 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col2" class="data row120 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col3" class="data row120 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col4" class="data row120 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col5" class="data row120 col5" >Isurriarap71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row120_col6" class="data row120 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row121" class="row_heading level0 row121" >121</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col0" class="data row121 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col1" class="data row121 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col2" class="data row121 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col3" class="data row121 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col4" class="data row121 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col5" class="data row121 col5" >Lassjask63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row121_col6" class="data row121 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row122" class="row_heading level0 row122" >122</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col0" class="data row122 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col1" class="data row122 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col2" class="data row122 col2" >53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col3" class="data row122 col3" >Vengeance Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col4" class="data row122 col4" >$3.70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col5" class="data row122 col5" >Iliel92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row122_col6" class="data row122 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row123" class="row_heading level0 row123" >123</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col0" class="data row123 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col1" class="data row123 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col2" class="data row123 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col3" class="data row123 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col4" class="data row123 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col5" class="data row123 col5" >Arithllorin55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row123_col6" class="data row123 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row124" class="row_heading level0 row124" >124</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col0" class="data row124 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col1" class="data row124 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col2" class="data row124 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col3" class="data row124 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col4" class="data row124 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col5" class="data row124 col5" >Silideu44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row124_col6" class="data row124 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row125" class="row_heading level0 row125" >125</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col0" class="data row125 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col1" class="data row125 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col2" class="data row125 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col3" class="data row125 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col4" class="data row125 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col5" class="data row125 col5" >Heosurnuru52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row125_col6" class="data row125 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row126" class="row_heading level0 row126" >126</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col0" class="data row126 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col1" class="data row126 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col2" class="data row126 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col3" class="data row126 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col4" class="data row126 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col5" class="data row126 col5" >Raesty92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row126_col6" class="data row126 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row127" class="row_heading level0 row127" >127</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col0" class="data row127 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col1" class="data row127 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col2" class="data row127 col2" >74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col3" class="data row127 col3" >Yearning Crusher</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col4" class="data row127 col4" >$1.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col5" class="data row127 col5" >Eyircil84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row127_col6" class="data row127 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row128" class="row_heading level0 row128" >128</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col0" class="data row128 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col1" class="data row128 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col2" class="data row128 col2" >140</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col3" class="data row128 col3" >Striker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col4" class="data row128 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col5" class="data row128 col5" >Isursti83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row128_col6" class="data row128 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row129" class="row_heading level0 row129" >129</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col0" class="data row129 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col1" class="data row129 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col2" class="data row129 col2" >126</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col3" class="data row129 col3" >Exiled Mithril Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col4" class="data row129 col4" >$3.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col5" class="data row129 col5" >Eurinu48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row129_col6" class="data row129 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row130" class="row_heading level0 row130" >130</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col0" class="data row130 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col1" class="data row130 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col2" class="data row130 col2" >50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col3" class="data row130 col3" >Dawn</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col4" class="data row130 col4" >$2.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col5" class="data row130 col5" >Saedaiphos46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row130_col6" class="data row130 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row131" class="row_heading level0 row131" >131</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col0" class="data row131 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col1" class="data row131 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col2" class="data row131 col2" >62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col3" class="data row131 col3" >Piece Maker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col4" class="data row131 col4" >$4.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col5" class="data row131 col5" >Undirrala66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row131_col6" class="data row131 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row132" class="row_heading level0 row132" >132</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col0" class="data row132 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col1" class="data row132 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col2" class="data row132 col2" >125</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col3" class="data row132 col3" >Whistling Mithril Warblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col4" class="data row132 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col5" class="data row132 col5" >Jiskossa51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row132_col6" class="data row132 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row133" class="row_heading level0 row133" >133</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col0" class="data row133 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col1" class="data row133 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col2" class="data row133 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col3" class="data row133 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col4" class="data row133 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col5" class="data row133 col5" >Sundossast30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row133_col6" class="data row133 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row134" class="row_heading level0 row134" >134</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col0" class="data row134 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col1" class="data row134 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col2" class="data row134 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col3" class="data row134 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col4" class="data row134 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col5" class="data row134 col5" >Ialallo29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row134_col6" class="data row134 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row135" class="row_heading level0 row135" >135</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col0" class="data row135 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col1" class="data row135 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col2" class="data row135 col2" >68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col3" class="data row135 col3" >Storm-Weaver, Slayer of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col4" class="data row135 col4" >$2.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col5" class="data row135 col5" >Syasriria69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row135_col6" class="data row135 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row136" class="row_heading level0 row136" >136</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col0" class="data row136 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col1" class="data row136 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col2" class="data row136 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col3" class="data row136 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col4" class="data row136 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col5" class="data row136 col5" >Chanosia60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row136_col6" class="data row136 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row137" class="row_heading level0 row137" >137</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col0" class="data row137 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col1" class="data row137 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col2" class="data row137 col2" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col3" class="data row137 col3" >Netherbane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col4" class="data row137 col4" >$1.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col5" class="data row137 col5" >Ilosia37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row137_col6" class="data row137 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row138" class="row_heading level0 row138" >138</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col0" class="data row138 col0" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col1" class="data row138 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col2" class="data row138 col2" >129</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col3" class="data row138 col3" >Fate, Vengeance of Eternal Justice</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col4" class="data row138 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col5" class="data row138 col5" >Tyeulisu40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row138_col6" class="data row138 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row139" class="row_heading level0 row139" >139</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col0" class="data row139 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col1" class="data row139 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col2" class="data row139 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col3" class="data row139 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col4" class="data row139 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col5" class="data row139 col5" >Yaliru88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row139_col6" class="data row139 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row140" class="row_heading level0 row140" >140</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col0" class="data row140 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col1" class="data row140 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col2" class="data row140 col2" >149</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col3" class="data row140 col3" >Tranquility, Razor of Black Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col4" class="data row140 col4" >$2.47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col5" class="data row140 col5" >Jiskassa76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row140_col6" class="data row140 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row141" class="row_heading level0 row141" >141</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col0" class="data row141 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col1" class="data row141 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col2" class="data row141 col2" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col3" class="data row141 col3" >Dawne</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col4" class="data row141 col4" >$4.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col5" class="data row141 col5" >Idairin80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row141_col6" class="data row141 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row142" class="row_heading level0 row142" >142</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col0" class="data row142 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col1" class="data row142 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col2" class="data row142 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col3" class="data row142 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col4" class="data row142 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col5" class="data row142 col5" >Dyally87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row142_col6" class="data row142 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row143" class="row_heading level0 row143" >143</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col0" class="data row143 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col1" class="data row143 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col2" class="data row143 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col3" class="data row143 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col4" class="data row143 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col5" class="data row143 col5" >Quarusrion32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row143_col6" class="data row143 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row144" class="row_heading level0 row144" >144</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col0" class="data row144 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col1" class="data row144 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col2" class="data row144 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col3" class="data row144 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col4" class="data row144 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col5" class="data row144 col5" >Adairialis76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row144_col6" class="data row144 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row145" class="row_heading level0 row145" >145</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col0" class="data row145 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col1" class="data row145 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col2" class="data row145 col2" >71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col3" class="data row145 col3" >Demise</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col4" class="data row145 col4" >$4.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col5" class="data row145 col5" >Lirtilsan89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row145_col6" class="data row145 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row146" class="row_heading level0 row146" >146</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col0" class="data row146 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col1" class="data row146 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col2" class="data row146 col2" >71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col3" class="data row146 col3" >Demise</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col4" class="data row146 col4" >$4.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col5" class="data row146 col5" >Reolacal36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row146_col6" class="data row146 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row147" class="row_heading level0 row147" >147</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col0" class="data row147 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col1" class="data row147 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col2" class="data row147 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col3" class="data row147 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col4" class="data row147 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col5" class="data row147 col5" >Chadanto83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row147_col6" class="data row147 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row148" class="row_heading level0 row148" >148</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col0" class="data row148 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col1" class="data row148 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col2" class="data row148 col2" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col3" class="data row148 col3" >Possessed Core</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col4" class="data row148 col4" >$1.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col5" class="data row148 col5" >Lisirrast82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row148_col6" class="data row148 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row149" class="row_heading level0 row149" >149</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col0" class="data row149 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col1" class="data row149 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col2" class="data row149 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col3" class="data row149 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col4" class="data row149 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col5" class="data row149 col5" >Ilrian97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row149_col6" class="data row149 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row150" class="row_heading level0 row150" >150</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col0" class="data row150 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col1" class="data row150 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col2" class="data row150 col2" >58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col3" class="data row150 col3" >Freak's Bite, Favor of Holy Might</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col4" class="data row150 col4" >$3.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col5" class="data row150 col5" >Tyadaru49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row150_col6" class="data row150 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row151" class="row_heading level0 row151" >151</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col0" class="data row151 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col1" class="data row151 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col2" class="data row151 col2" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col3" class="data row151 col3" >Shadow Strike, Glory of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col4" class="data row151 col4" >$1.93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col5" class="data row151 col5" >Sweecossa42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row151_col6" class="data row151 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row152" class="row_heading level0 row152" >152</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col0" class="data row152 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col1" class="data row152 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col2" class="data row152 col2" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col3" class="data row152 col3" >Lazarus, Terror of the Earth</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col4" class="data row152 col4" >$3.47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col5" class="data row152 col5" >Streural92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row152_col6" class="data row152 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row153" class="row_heading level0 row153" >153</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col0" class="data row153 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col1" class="data row153 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col2" class="data row153 col2" >155</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col3" class="data row153 col3" >War-Forged Gold Deflector</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col4" class="data row153 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col5" class="data row153 col5" >Queusurra38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row153_col6" class="data row153 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row154" class="row_heading level0 row154" >154</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col0" class="data row154 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col1" class="data row154 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col2" class="data row154 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col3" class="data row154 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col4" class="data row154 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col5" class="data row154 col5" >Lassilsa41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row154_col6" class="data row154 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row155" class="row_heading level0 row155" >155</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col0" class="data row155 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col1" class="data row155 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col2" class="data row155 col2" >105</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col3" class="data row155 col3" >Hailstorm Shadowsteel Scythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col4" class="data row155 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col5" class="data row155 col5" >Aisurphos78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row155_col6" class="data row155 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row156" class="row_heading level0 row156" >156</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col0" class="data row156 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col1" class="data row156 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col2" class="data row156 col2" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col3" class="data row156 col3" >Riddle, Tribute of Ended Dreams</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col4" class="data row156 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col5" class="data row156 col5" >Marim28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row156_col6" class="data row156 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row157" class="row_heading level0 row157" >157</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col0" class="data row157 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col1" class="data row157 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col2" class="data row157 col2" >52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col3" class="data row157 col3" >Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col4" class="data row157 col4" >$4.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col5" class="data row157 col5" >Taeduenu92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row157_col6" class="data row157 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row158" class="row_heading level0 row158" >158</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col0" class="data row158 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col1" class="data row158 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col2" class="data row158 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col3" class="data row158 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col4" class="data row158 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col5" class="data row158 col5" >Eodailis27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row158_col6" class="data row158 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row159" class="row_heading level0 row159" >159</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col0" class="data row159 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col1" class="data row159 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col2" class="data row159 col2" >100</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col3" class="data row159 col3" >Blindscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col4" class="data row159 col4" >$3.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col5" class="data row159 col5" >Lassjaskan73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row159_col6" class="data row159 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row160" class="row_heading level0 row160" >160</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col0" class="data row160 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col1" class="data row160 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col2" class="data row160 col2" >112</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col3" class="data row160 col3" >Worldbreaker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col4" class="data row160 col4" >$3.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col5" class="data row160 col5" >Yadanun74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row160_col6" class="data row160 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row161" class="row_heading level0 row161" >161</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col0" class="data row161 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col1" class="data row161 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col2" class="data row161 col2" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col3" class="data row161 col3" >Warped Fetish</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col4" class="data row161 col4" >$2.41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col5" class="data row161 col5" >Iskossasda43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row161_col6" class="data row161 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row162" class="row_heading level0 row162" >162</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col0" class="data row162 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col1" class="data row162 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col2" class="data row162 col2" >94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col3" class="data row162 col3" >Mourning Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col4" class="data row162 col4" >$1.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col5" class="data row162 col5" >Aesty51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row162_col6" class="data row162 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row163" class="row_heading level0 row163" >163</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col0" class="data row163 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col1" class="data row163 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col2" class="data row163 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col3" class="data row163 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col4" class="data row163 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col5" class="data row163 col5" >Tyida79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row163_col6" class="data row163 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row164" class="row_heading level0 row164" >164</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col0" class="data row164 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col1" class="data row164 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col2" class="data row164 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col3" class="data row164 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col4" class="data row164 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col5" class="data row164 col5" >Frichossast75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row164_col6" class="data row164 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row165" class="row_heading level0 row165" >165</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col0" class="data row165 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col1" class="data row165 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col2" class="data row165 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col3" class="data row165 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col4" class="data row165 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col5" class="data row165 col5" >Eratiel90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row165_col6" class="data row165 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row166" class="row_heading level0 row166" >166</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col0" class="data row166 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col1" class="data row166 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col2" class="data row166 col2" >173</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col3" class="data row166 col3" >Stormfury Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col4" class="data row166 col4" >$4.83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col5" class="data row166 col5" >Eoda93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row166_col6" class="data row166 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row167" class="row_heading level0 row167" >167</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col0" class="data row167 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col1" class="data row167 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col2" class="data row167 col2" >86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col3" class="data row167 col3" >Stormfury Lantern</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col4" class="data row167 col4" >$1.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col5" class="data row167 col5" >Chamirra53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row167_col6" class="data row167 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row168" class="row_heading level0 row168" >168</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col0" class="data row168 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col1" class="data row168 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col2" class="data row168 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col3" class="data row168 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col4" class="data row168 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col5" class="data row168 col5" >Alarap40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row168_col6" class="data row168 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row169" class="row_heading level0 row169" >169</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col0" class="data row169 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col1" class="data row169 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col2" class="data row169 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col3" class="data row169 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col4" class="data row169 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col5" class="data row169 col5" >Ralaeriadeu65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row169_col6" class="data row169 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row170" class="row_heading level0 row170" >170</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col0" class="data row170 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col1" class="data row170 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col2" class="data row170 col2" >71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col3" class="data row170 col3" >Demise</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col4" class="data row170 col4" >$4.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col5" class="data row170 col5" >Reulae52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row170_col6" class="data row170 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row171" class="row_heading level0 row171" >171</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col0" class="data row171 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col1" class="data row171 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col2" class="data row171 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col3" class="data row171 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col4" class="data row171 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col5" class="data row171 col5" >Stryanastip77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row171_col6" class="data row171 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row172" class="row_heading level0 row172" >172</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col0" class="data row172 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col1" class="data row172 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col2" class="data row172 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col3" class="data row172 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col4" class="data row172 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col5" class="data row172 col5" >Iskirra45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row172_col6" class="data row172 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row173" class="row_heading level0 row173" >173</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col0" class="data row173 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col1" class="data row173 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col2" class="data row173 col2" >0</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col3" class="data row173 col3" >Splinter</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col4" class="data row173 col4" >$1.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col5" class="data row173 col5" >Chadadarya31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row173_col6" class="data row173 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row174" class="row_heading level0 row174" >174</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col0" class="data row174 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col1" class="data row174 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col2" class="data row174 col2" >182</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col3" class="data row174 col3" >Toothpick</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col4" class="data row174 col4" >$3.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col5" class="data row174 col5" >Heuli25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row174_col6" class="data row174 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row175" class="row_heading level0 row175" >175</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col0" class="data row175 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col1" class="data row175 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col2" class="data row175 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col3" class="data row175 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col4" class="data row175 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col5" class="data row175 col5" >Raillydeu47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row175_col6" class="data row175 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row176" class="row_heading level0 row176" >176</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col0" class="data row176 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col1" class="data row176 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col2" class="data row176 col2" >182</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col3" class="data row176 col3" >Toothpick</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col4" class="data row176 col4" >$3.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col5" class="data row176 col5" >Chamadar61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row176_col6" class="data row176 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row177" class="row_heading level0 row177" >177</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col0" class="data row177 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col1" class="data row177 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col2" class="data row177 col2" >155</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col3" class="data row177 col3" >War-Forged Gold Deflector</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col4" class="data row177 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col5" class="data row177 col5" >Assassa38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row177_col6" class="data row177 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row178" class="row_heading level0 row178" >178</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col0" class="data row178 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col1" class="data row178 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col2" class="data row178 col2" >97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col3" class="data row178 col3" >Swan Song, Gouger Of Terror</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col4" class="data row178 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col5" class="data row178 col5" >Shaidanu32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row178_col6" class="data row178 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row179" class="row_heading level0 row179" >179</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col0" class="data row179 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col1" class="data row179 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col2" class="data row179 col2" >70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col3" class="data row179 col3" >Hope's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col4" class="data row179 col4" >$3.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col5" class="data row179 col5" >Chanosiaya39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row179_col6" class="data row179 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row180" class="row_heading level0 row180" >180</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col0" class="data row180 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col1" class="data row180 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col2" class="data row180 col2" >89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col3" class="data row180 col3" >Blazefury, Protector of Delusions</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col4" class="data row180 col4" >$1.50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col5" class="data row180 col5" >Raeri71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row180_col6" class="data row180 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row181" class="row_heading level0 row181" >181</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col0" class="data row181 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col1" class="data row181 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col2" class="data row181 col2" >1</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col3" class="data row181 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col4" class="data row181 col4" >$2.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col5" class="data row181 col5" >Hiasri33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row181_col6" class="data row181 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row182" class="row_heading level0 row182" >182</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col0" class="data row182 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col1" class="data row182 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col2" class="data row182 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col3" class="data row182 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col4" class="data row182 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col5" class="data row182 col5" >Lisossa25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row182_col6" class="data row182 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row183" class="row_heading level0 row183" >183</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col0" class="data row183 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col1" class="data row183 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col2" class="data row183 col2" >87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col3" class="data row183 col3" >Deluge, Edge of the West</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col4" class="data row183 col4" >$2.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col5" class="data row183 col5" >Sundassa93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row183_col6" class="data row183 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row184" class="row_heading level0 row184" >184</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col0" class="data row184 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col1" class="data row184 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col2" class="data row184 col2" >170</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col3" class="data row184 col3" >Shadowsteel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col4" class="data row184 col4" >$1.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col5" class="data row184 col5" >Rina82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row184_col6" class="data row184 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row185" class="row_heading level0 row185" >185</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col0" class="data row185 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col1" class="data row185 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col2" class="data row185 col2" >167</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col3" class="data row185 col3" >Malice, Legacy of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col4" class="data row185 col4" >$2.38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col5" class="data row185 col5" >Siarinum43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row185_col6" class="data row185 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row186" class="row_heading level0 row186" >186</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col0" class="data row186 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col1" class="data row186 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col2" class="data row186 col2" >144</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col3" class="data row186 col3" >Blood Infused Guardian</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col4" class="data row186 col4" >$2.86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col5" class="data row186 col5" >Chanosiaya39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row186_col6" class="data row186 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row187" class="row_heading level0 row187" >187</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col0" class="data row187 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col1" class="data row187 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col2" class="data row187 col2" >93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col3" class="data row187 col3" >Apocalyptic Battlescythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col4" class="data row187 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col5" class="data row187 col5" >Eurallo89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row187_col6" class="data row187 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row188" class="row_heading level0 row188" >188</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col0" class="data row188 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col1" class="data row188 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col2" class="data row188 col2" >78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col3" class="data row188 col3" >Glimmer, Ender of the Moon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col4" class="data row188 col4" >$2.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col5" class="data row188 col5" >Hirirap39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row188_col6" class="data row188 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row189" class="row_heading level0 row189" >189</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col0" class="data row189 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col1" class="data row189 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col2" class="data row189 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col3" class="data row189 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col4" class="data row189 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col5" class="data row189 col5" >Raillydeu47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row189_col6" class="data row189 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row190" class="row_heading level0 row190" >190</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col0" class="data row190 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col1" class="data row190 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col2" class="data row190 col2" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col3" class="data row190 col3" >Spectral Bone Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col4" class="data row190 col4" >$2.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col5" class="data row190 col5" >Frichaya88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row190_col6" class="data row190 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row191" class="row_heading level0 row191" >191</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col0" class="data row191 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col1" class="data row191 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col2" class="data row191 col2" >75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col3" class="data row191 col3" >Brutality Ivory Warmace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col4" class="data row191 col4" >$1.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col5" class="data row191 col5" >Aidaira26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row191_col6" class="data row191 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row192" class="row_heading level0 row192" >192</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col0" class="data row192 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col1" class="data row192 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col2" class="data row192 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col3" class="data row192 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col4" class="data row192 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col5" class="data row192 col5" >Zontibe81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row192_col6" class="data row192 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row193" class="row_heading level0 row193" >193</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col0" class="data row193 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col1" class="data row193 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col2" class="data row193 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col3" class="data row193 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col4" class="data row193 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col5" class="data row193 col5" >Farusrian86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row193_col6" class="data row193 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row194" class="row_heading level0 row194" >194</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col0" class="data row194 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col1" class="data row194 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col2" class="data row194 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col3" class="data row194 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col4" class="data row194 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col5" class="data row194 col5" >Undadarla37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row194_col6" class="data row194 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row195" class="row_heading level0 row195" >195</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col0" class="data row195 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col1" class="data row195 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col2" class="data row195 col2" >160</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col3" class="data row195 col3" >Azurewrath</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col4" class="data row195 col4" >$2.22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col5" class="data row195 col5" >Lirtossa78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row195_col6" class="data row195 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row196" class="row_heading level0 row196" >196</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col0" class="data row196 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col1" class="data row196 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col2" class="data row196 col2" >89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col3" class="data row196 col3" >Blazefury, Protector of Delusions</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col4" class="data row196 col4" >$1.50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col5" class="data row196 col5" >Chanirra56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row196_col6" class="data row196 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row197" class="row_heading level0 row197" >197</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col0" class="data row197 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col1" class="data row197 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col2" class="data row197 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col3" class="data row197 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col4" class="data row197 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col5" class="data row197 col5" >Lassast89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row197_col6" class="data row197 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row198" class="row_heading level0 row198" >198</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col0" class="data row198 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col1" class="data row198 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col2" class="data row198 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col3" class="data row198 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col4" class="data row198 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col5" class="data row198 col5" >Lisasi93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row198_col6" class="data row198 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row199" class="row_heading level0 row199" >199</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col0" class="data row199 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col1" class="data row199 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col2" class="data row199 col2" >180</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col3" class="data row199 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col4" class="data row199 col4" >$2.78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col5" class="data row199 col5" >Phadai31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row199_col6" class="data row199 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row200" class="row_heading level0 row200" >200</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col0" class="data row200 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col1" class="data row200 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col2" class="data row200 col2" >143</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col3" class="data row200 col3" >Frenzied Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col4" class="data row200 col4" >$2.60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col5" class="data row200 col5" >Tyithesura58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row200_col6" class="data row200 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row201" class="row_heading level0 row201" >201</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col0" class="data row201 col0" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col1" class="data row201 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col2" class="data row201 col2" >137</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col3" class="data row201 col3" >Aetherius, Boon of the Blessed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col4" class="data row201 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col5" class="data row201 col5" >Marilsa48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row201_col6" class="data row201 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row202" class="row_heading level0 row202" >202</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col0" class="data row202 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col1" class="data row202 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col2" class="data row202 col2" >176</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col3" class="data row202 col3" >Relentless Iron Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col4" class="data row202 col4" >$2.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col5" class="data row202 col5" >Siarithria38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row202_col6" class="data row202 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row203" class="row_heading level0 row203" >203</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col0" class="data row203 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col1" class="data row203 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col2" class="data row203 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col3" class="data row203 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col4" class="data row203 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col5" class="data row203 col5" >Lisasi93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row203_col6" class="data row203 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row204" class="row_heading level0 row204" >204</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col0" class="data row204 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col1" class="data row204 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col2" class="data row204 col2" >127</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col3" class="data row204 col3" >Heartseeker, Reaver of Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col4" class="data row204 col4" >$3.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col5" class="data row204 col5" >Marirrasta50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row204_col6" class="data row204 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row205" class="row_heading level0 row205" >205</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col0" class="data row205 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col1" class="data row205 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col2" class="data row205 col2" >147</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col3" class="data row205 col3" >Hellreaver, Heirloom of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col4" class="data row205 col4" >$3.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col5" class="data row205 col5" >Airidil41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row205_col6" class="data row205 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row206" class="row_heading level0 row206" >206</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col0" class="data row206 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col1" class="data row206 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col2" class="data row206 col2" >161</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col3" class="data row206 col3" >Devine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col4" class="data row206 col4" >$1.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col5" class="data row206 col5" >Sausosia74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row206_col6" class="data row206 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row207" class="row_heading level0 row207" >207</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col0" class="data row207 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col1" class="data row207 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col2" class="data row207 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col3" class="data row207 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col4" class="data row207 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col5" class="data row207 col5" >Yadanun74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row207_col6" class="data row207 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row208" class="row_heading level0 row208" >208</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col0" class="data row208 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col1" class="data row208 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col2" class="data row208 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col3" class="data row208 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col4" class="data row208 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col5" class="data row208 col5" >Sialaera37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row208_col6" class="data row208 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row209" class="row_heading level0 row209" >209</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col0" class="data row209 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col1" class="data row209 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col2" class="data row209 col2" >157</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col3" class="data row209 col3" >Spada, Etcher of Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col4" class="data row209 col4" >$2.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col5" class="data row209 col5" >Frichistasta59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row209_col6" class="data row209 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row210" class="row_heading level0 row210" >210</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col0" class="data row210 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col1" class="data row210 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col2" class="data row210 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col3" class="data row210 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col4" class="data row210 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col5" class="data row210 col5" >Phadue96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row210_col6" class="data row210 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row211" class="row_heading level0 row211" >211</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col0" class="data row211 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col1" class="data row211 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col2" class="data row211 col2" >176</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col3" class="data row211 col3" >Relentless Iron Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col4" class="data row211 col4" >$2.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col5" class="data row211 col5" >Chanirra79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row211_col6" class="data row211 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row212" class="row_heading level0 row212" >212</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col0" class="data row212 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col1" class="data row212 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col2" class="data row212 col2" >111</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col3" class="data row212 col3" >Misery's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col4" class="data row212 col4" >$2.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col5" class="data row212 col5" >Yarmol79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row212_col6" class="data row212 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row213" class="row_heading level0 row213" >213</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col0" class="data row213 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col1" class="data row213 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col2" class="data row213 col2" >127</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col3" class="data row213 col3" >Heartseeker, Reaver of Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col4" class="data row213 col4" >$3.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col5" class="data row213 col5" >Astydil38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row213_col6" class="data row213 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row214" class="row_heading level0 row214" >214</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col0" class="data row214 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col1" class="data row214 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col2" class="data row214 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col3" class="data row214 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col4" class="data row214 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col5" class="data row214 col5" >Jiskirran77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row214_col6" class="data row214 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row215" class="row_heading level0 row215" >215</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col0" class="data row215 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col1" class="data row215 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col2" class="data row215 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col3" class="data row215 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col4" class="data row215 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col5" class="data row215 col5" >Marjasksda39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row215_col6" class="data row215 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row216" class="row_heading level0 row216" >216</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col0" class="data row216 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col1" class="data row216 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col2" class="data row216 col2" >116</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col3" class="data row216 col3" >Renewed Skeletal Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col4" class="data row216 col4" >$2.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col5" class="data row216 col5" >Eoralphos86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row216_col6" class="data row216 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row217" class="row_heading level0 row217" >217</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col0" class="data row217 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col1" class="data row217 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col2" class="data row217 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col3" class="data row217 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col4" class="data row217 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col5" class="data row217 col5" >Lisovynya38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row217_col6" class="data row217 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row218" class="row_heading level0 row218" >218</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col0" class="data row218 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col1" class="data row218 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col2" class="data row218 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col3" class="data row218 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col4" class="data row218 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col5" class="data row218 col5" >Hailaphos89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row218_col6" class="data row218 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row219" class="row_heading level0 row219" >219</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col0" class="data row219 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col1" class="data row219 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col2" class="data row219 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col3" class="data row219 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col4" class="data row219 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col5" class="data row219 col5" >Frichim77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row219_col6" class="data row219 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row220" class="row_heading level0 row220" >220</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col0" class="data row220 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col1" class="data row220 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col2" class="data row220 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col3" class="data row220 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col4" class="data row220 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col5" class="data row220 col5" >Aellyrialis39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row220_col6" class="data row220 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row221" class="row_heading level0 row221" >221</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col0" class="data row221 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col1" class="data row221 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col2" class="data row221 col2" >61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col3" class="data row221 col3" >Ragnarok</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col4" class="data row221 col4" >$3.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col5" class="data row221 col5" >Chamilsan75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row221_col6" class="data row221 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row222" class="row_heading level0 row222" >222</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col0" class="data row222 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col1" class="data row222 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col2" class="data row222 col2" >131</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col3" class="data row222 col3" >Fury</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col4" class="data row222 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col5" class="data row222 col5" >Saida58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row222_col6" class="data row222 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row223" class="row_heading level0 row223" >223</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col0" class="data row223 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col1" class="data row223 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col2" class="data row223 col2" >41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col3" class="data row223 col3" >Orbit</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col4" class="data row223 col4" >$1.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col5" class="data row223 col5" >Eusri70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row223_col6" class="data row223 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row224" class="row_heading level0 row224" >224</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col0" class="data row224 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col1" class="data row224 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col2" class="data row224 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col3" class="data row224 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col4" class="data row224 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col5" class="data row224 col5" >Aeduera68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row224_col6" class="data row224 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row225" class="row_heading level0 row225" >225</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col0" class="data row225 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col1" class="data row225 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col2" class="data row225 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col3" class="data row225 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col4" class="data row225 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col5" class="data row225 col5" >Qilatie51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row225_col6" class="data row225 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row226" class="row_heading level0 row226" >226</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col0" class="data row226 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col1" class="data row226 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col2" class="data row226 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col3" class="data row226 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col4" class="data row226 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col5" class="data row226 col5" >Chamistast30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row226_col6" class="data row226 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row227" class="row_heading level0 row227" >227</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col0" class="data row227 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col1" class="data row227 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col2" class="data row227 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col3" class="data row227 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col4" class="data row227 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col5" class="data row227 col5" >Qiluard68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row227_col6" class="data row227 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row228" class="row_heading level0 row228" >228</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col0" class="data row228 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col1" class="data row228 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col2" class="data row228 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col3" class="data row228 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col4" class="data row228 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col5" class="data row228 col5" >Tyaelo67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row228_col6" class="data row228 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row229" class="row_heading level0 row229" >229</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col0" class="data row229 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col1" class="data row229 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col2" class="data row229 col2" >129</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col3" class="data row229 col3" >Fate, Vengeance of Eternal Justice</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col4" class="data row229 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col5" class="data row229 col5" >Rithe77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row229_col6" class="data row229 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row230" class="row_heading level0 row230" >230</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col0" class="data row230 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col1" class="data row230 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col2" class="data row230 col2" >140</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col3" class="data row230 col3" >Striker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col4" class="data row230 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col5" class="data row230 col5" >Tyeosristi57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row230_col6" class="data row230 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row231" class="row_heading level0 row231" >231</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col0" class="data row231 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col1" class="data row231 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col2" class="data row231 col2" >125</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col3" class="data row231 col3" >Whistling Mithril Warblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col4" class="data row231 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col5" class="data row231 col5" >Lassjaskan73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row231_col6" class="data row231 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row232" class="row_heading level0 row232" >232</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col0" class="data row232 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col1" class="data row232 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col2" class="data row232 col2" >60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col3" class="data row232 col3" >Wolf</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col4" class="data row232 col4" >$1.84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col5" class="data row232 col5" >Eoral49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row232_col6" class="data row232 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row233" class="row_heading level0 row233" >233</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col0" class="data row233 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col1" class="data row233 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col2" class="data row233 col2" >129</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col3" class="data row233 col3" >Fate, Vengeance of Eternal Justice</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col4" class="data row233 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col5" class="data row233 col5" >Aelollo59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row233_col6" class="data row233 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row234" class="row_heading level0 row234" >234</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col0" class="data row234 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col1" class="data row234 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col2" class="data row234 col2" >123</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col3" class="data row234 col3" >Twilight's Carver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col4" class="data row234 col4" >$1.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col5" class="data row234 col5" >Lisossa63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row234_col6" class="data row234 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row235" class="row_heading level0 row235" >235</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col0" class="data row235 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col1" class="data row235 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col2" class="data row235 col2" >162</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col3" class="data row235 col3" >Abyssal Shard</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col4" class="data row235 col4" >$2.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col5" class="data row235 col5" >Wailin72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row235_col6" class="data row235 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row236" class="row_heading level0 row236" >236</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col0" class="data row236 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col1" class="data row236 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col2" class="data row236 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col3" class="data row236 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col4" class="data row236 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col5" class="data row236 col5" >Yarithllodeu72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row236_col6" class="data row236 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row237" class="row_heading level0 row237" >237</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col0" class="data row237 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col1" class="data row237 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col2" class="data row237 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col3" class="data row237 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col4" class="data row237 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col5" class="data row237 col5" >Lisistaya47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row237_col6" class="data row237 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row238" class="row_heading level0 row238" >238</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col0" class="data row238 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col1" class="data row238 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col2" class="data row238 col2" >49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col3" class="data row238 col3" >The Oculus, Token of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col4" class="data row238 col4" >$4.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col5" class="data row238 col5" >Chamadar27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row238_col6" class="data row238 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row239" class="row_heading level0 row239" >239</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col0" class="data row239 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col1" class="data row239 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col2" class="data row239 col2" >58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col3" class="data row239 col3" >Freak's Bite, Favor of Holy Might</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col4" class="data row239 col4" >$3.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col5" class="data row239 col5" >Ethruard50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row239_col6" class="data row239 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row240" class="row_heading level0 row240" >240</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col0" class="data row240 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col1" class="data row240 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col2" class="data row240 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col3" class="data row240 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col4" class="data row240 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col5" class="data row240 col5" >Lisossa63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row240_col6" class="data row240 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row241" class="row_heading level0 row241" >241</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col0" class="data row241 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col1" class="data row241 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col2" class="data row241 col2" >135</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col3" class="data row241 col3" >Warped Diamond Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col4" class="data row241 col4" >$4.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col5" class="data row241 col5" >Yathecal72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row241_col6" class="data row241 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row242" class="row_heading level0 row242" >242</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col0" class="data row242 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col1" class="data row242 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col2" class="data row242 col2" >182</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col3" class="data row242 col3" >Toothpick</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col4" class="data row242 col4" >$3.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col5" class="data row242 col5" >Ilimya66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row242_col6" class="data row242 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row243" class="row_heading level0 row243" >243</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col0" class="data row243 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col1" class="data row243 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col2" class="data row243 col2" >157</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col3" class="data row243 col3" >Spada, Etcher of Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col4" class="data row243 col4" >$2.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col5" class="data row243 col5" >Ialistidru50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row243_col6" class="data row243 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row244" class="row_heading level0 row244" >244</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col0" class="data row244 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col1" class="data row244 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col2" class="data row244 col2" >183</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col3" class="data row244 col3" >Dragon's Greatsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col4" class="data row244 col4" >$2.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col5" class="data row244 col5" >Tyaerith73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row244_col6" class="data row244 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row245" class="row_heading level0 row245" >245</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col0" class="data row245 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col1" class="data row245 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col2" class="data row245 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col3" class="data row245 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col4" class="data row245 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col5" class="data row245 col5" >Lisistasya93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row245_col6" class="data row245 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row246" class="row_heading level0 row246" >246</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col0" class="data row246 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col1" class="data row246 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col2" class="data row246 col2" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col3" class="data row246 col3" >Dawne</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col4" class="data row246 col4" >$4.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col5" class="data row246 col5" >Chamadar79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row246_col6" class="data row246 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row247" class="row_heading level0 row247" >247</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col0" class="data row247 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col1" class="data row247 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col2" class="data row247 col2" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col3" class="data row247 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col4" class="data row247 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col5" class="data row247 col5" >Haerith37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row247_col6" class="data row247 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row248" class="row_heading level0 row248" >248</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col0" class="data row248 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col1" class="data row248 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col2" class="data row248 col2" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col3" class="data row248 col3" >Second Chance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col4" class="data row248 col4" >$2.34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col5" class="data row248 col5" >Iallyphos37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row248_col6" class="data row248 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row249" class="row_heading level0 row249" >249</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col0" class="data row249 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col1" class="data row249 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col2" class="data row249 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col3" class="data row249 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col4" class="data row249 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col5" class="data row249 col5" >Tyaelo67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row249_col6" class="data row249 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row250" class="row_heading level0 row250" >250</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col0" class="data row250 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col1" class="data row250 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col2" class="data row250 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col3" class="data row250 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col4" class="data row250 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col5" class="data row250 col5" >Ilogha82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row250_col6" class="data row250 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row251" class="row_heading level0 row251" >251</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col0" class="data row251 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col1" class="data row251 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col2" class="data row251 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col3" class="data row251 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col4" class="data row251 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col5" class="data row251 col5" >Aeri84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row251_col6" class="data row251 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row252" class="row_heading level0 row252" >252</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col0" class="data row252 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col1" class="data row252 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col2" class="data row252 col2" >1</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col3" class="data row252 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col4" class="data row252 col4" >$2.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col5" class="data row252 col5" >Ilaesudil92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row252_col6" class="data row252 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row253" class="row_heading level0 row253" >253</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col0" class="data row253 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col1" class="data row253 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col2" class="data row253 col2" >149</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col3" class="data row253 col3" >Tranquility, Razor of Black Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col4" class="data row253 col4" >$2.47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col5" class="data row253 col5" >Meosridil82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row253_col6" class="data row253 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row254" class="row_heading level0 row254" >254</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col0" class="data row254 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col1" class="data row254 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col2" class="data row254 col2" >1</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col3" class="data row254 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col4" class="data row254 col4" >$2.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col5" class="data row254 col5" >Undirrasta89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row254_col6" class="data row254 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row255" class="row_heading level0 row255" >255</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col0" class="data row255 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col1" class="data row255 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col2" class="data row255 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col3" class="data row255 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col4" class="data row255 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col5" class="data row255 col5" >Lirtistanya48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row255_col6" class="data row255 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row256" class="row_heading level0 row256" >256</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col0" class="data row256 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col1" class="data row256 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col2" class="data row256 col2" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col3" class="data row256 col3" >Lazarus, Terror of the Earth</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col4" class="data row256 col4" >$3.47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col5" class="data row256 col5" >Iadueria43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row256_col6" class="data row256 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row257" class="row_heading level0 row257" >257</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col0" class="data row257 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col1" class="data row257 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col2" class="data row257 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col3" class="data row257 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col4" class="data row257 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col5" class="data row257 col5" >Chanirrala39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row257_col6" class="data row257 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row258" class="row_heading level0 row258" >258</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col0" class="data row258 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col1" class="data row258 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col2" class="data row258 col2" >97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col3" class="data row258 col3" >Swan Song, Gouger Of Terror</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col4" class="data row258 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col5" class="data row258 col5" >Lisjaskan36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row258_col6" class="data row258 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row259" class="row_heading level0 row259" >259</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col0" class="data row259 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col1" class="data row259 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col2" class="data row259 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col3" class="data row259 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col4" class="data row259 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col5" class="data row259 col5" >Saedue76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row259_col6" class="data row259 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row260" class="row_heading level0 row260" >260</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col0" class="data row260 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col1" class="data row260 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col2" class="data row260 col2" >99</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col3" class="data row260 col3" >Expiration, Warscythe Of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col4" class="data row260 col4" >$4.53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col5" class="data row260 col5" >Undjasksya56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row260_col6" class="data row260 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row261" class="row_heading level0 row261" >261</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col0" class="data row261 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col1" class="data row261 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col2" class="data row261 col2" >46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col3" class="data row261 col3" >Hopeless Ebon Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col4" class="data row261 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col5" class="data row261 col5" >Irithrap69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row261_col6" class="data row261 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row262" class="row_heading level0 row262" >262</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col0" class="data row262 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col1" class="data row262 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col2" class="data row262 col2" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col3" class="data row262 col3" >Chaos, Ender of the End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col4" class="data row262 col4" >$3.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col5" class="data row262 col5" >Quanenrian83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row262_col6" class="data row262 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row263" class="row_heading level0 row263" >263</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col0" class="data row263 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col1" class="data row263 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col2" class="data row263 col2" >137</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col3" class="data row263 col3" >Aetherius, Boon of the Blessed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col4" class="data row263 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col5" class="data row263 col5" >Phenastya51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row263_col6" class="data row263 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row264" class="row_heading level0 row264" >264</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col0" class="data row264 col0" >45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col1" class="data row264 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col2" class="data row264 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col3" class="data row264 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col4" class="data row264 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col5" class="data row264 col5" >Marassaya49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row264_col6" class="data row264 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row265" class="row_heading level0 row265" >265</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col0" class="data row265 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col1" class="data row265 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col2" class="data row265 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col3" class="data row265 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col4" class="data row265 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col5" class="data row265 col5" >Saellyra72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row265_col6" class="data row265 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row266" class="row_heading level0 row266" >266</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col0" class="data row266 col0" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col1" class="data row266 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col2" class="data row266 col2" >143</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col3" class="data row266 col3" >Frenzied Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col4" class="data row266 col4" >$2.60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col5" class="data row266 col5" >Yasrisu92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row266_col6" class="data row266 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row267" class="row_heading level0 row267" >267</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col0" class="data row267 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col1" class="data row267 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col2" class="data row267 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col3" class="data row267 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col4" class="data row267 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col5" class="data row267 col5" >Frichistasta59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row267_col6" class="data row267 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row268" class="row_heading level0 row268" >268</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col0" class="data row268 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col1" class="data row268 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col2" class="data row268 col2" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col3" class="data row268 col3" >Spectral Bone Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col4" class="data row268 col4" >$2.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col5" class="data row268 col5" >Qilanrion65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row268_col6" class="data row268 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row269" class="row_heading level0 row269" >269</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col0" class="data row269 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col1" class="data row269 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col2" class="data row269 col2" >72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col3" class="data row269 col3" >Winter's Bite</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col4" class="data row269 col4" >$1.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col5" class="data row269 col5" >Chanassa48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row269_col6" class="data row269 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row270" class="row_heading level0 row270" >270</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col0" class="data row270 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col1" class="data row270 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col2" class="data row270 col2" >114</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col3" class="data row270 col3" >Yearning Mageblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col4" class="data row270 col4" >$1.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col5" class="data row270 col5" >Iskassa50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row270_col6" class="data row270 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row271" class="row_heading level0 row271" >271</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col0" class="data row271 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col1" class="data row271 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col2" class="data row271 col2" >77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col3" class="data row271 col3" >Piety, Guardian of Riddles</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col4" class="data row271 col4" >$3.68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col5" class="data row271 col5" >Frichjaskan98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row271_col6" class="data row271 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row272" class="row_heading level0 row272" >272</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col0" class="data row272 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col1" class="data row272 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col2" class="data row272 col2" >117</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col3" class="data row272 col3" >Heartstriker, Legacy of the Light</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col4" class="data row272 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col5" class="data row272 col5" >Sirira97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row272_col6" class="data row272 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row273" class="row_heading level0 row273" >273</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col0" class="data row273 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col1" class="data row273 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col2" class="data row273 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col3" class="data row273 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col4" class="data row273 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col5" class="data row273 col5" >Eoduenurin62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row273_col6" class="data row273 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row274" class="row_heading level0 row274" >274</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col0" class="data row274 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col1" class="data row274 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col2" class="data row274 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col3" class="data row274 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col4" class="data row274 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col5" class="data row274 col5" >Yarirarn35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row274_col6" class="data row274 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row275" class="row_heading level0 row275" >275</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col0" class="data row275 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col1" class="data row275 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col2" class="data row275 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col3" class="data row275 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col4" class="data row275 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col5" class="data row275 col5" >Yadanun74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row275_col6" class="data row275 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row276" class="row_heading level0 row276" >276</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col0" class="data row276 col0" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col1" class="data row276 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col2" class="data row276 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col3" class="data row276 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col4" class="data row276 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col5" class="data row276 col5" >Aillycal84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row276_col6" class="data row276 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row277" class="row_heading level0 row277" >277</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col0" class="data row277 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col1" class="data row277 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col2" class="data row277 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col3" class="data row277 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col4" class="data row277 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col5" class="data row277 col5" >Eosur70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row277_col6" class="data row277 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row278" class="row_heading level0 row278" >278</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col0" class="data row278 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col1" class="data row278 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col2" class="data row278 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col3" class="data row278 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col4" class="data row278 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col5" class="data row278 col5" >Chanadar44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row278_col6" class="data row278 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row279" class="row_heading level0 row279" >279</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col0" class="data row279 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col1" class="data row279 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col2" class="data row279 col2" >171</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col3" class="data row279 col3" >Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col4" class="data row279 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col5" class="data row279 col5" >Lisimsda29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row279_col6" class="data row279 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row280" class="row_heading level0 row280" >280</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col0" class="data row280 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col1" class="data row280 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col2" class="data row280 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col3" class="data row280 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col4" class="data row280 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col5" class="data row280 col5" >Tyidue95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row280_col6" class="data row280 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row281" class="row_heading level0 row281" >281</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col0" class="data row281 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col1" class="data row281 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col2" class="data row281 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col3" class="data row281 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col4" class="data row281 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col5" class="data row281 col5" >Yaralnura48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row281_col6" class="data row281 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row282" class="row_heading level0 row282" >282</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col0" class="data row282 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col1" class="data row282 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col2" class="data row282 col2" >48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col3" class="data row282 col3" >Rage, Legacy of the Lone Victor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col4" class="data row282 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col5" class="data row282 col5" >Irillo49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row282_col6" class="data row282 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row283" class="row_heading level0 row283" >283</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col0" class="data row283 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col1" class="data row283 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col2" class="data row283 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col3" class="data row283 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col4" class="data row283 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col5" class="data row283 col5" >Isri59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row283_col6" class="data row283 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row284" class="row_heading level0 row284" >284</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col0" class="data row284 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col1" class="data row284 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col2" class="data row284 col2" >88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col3" class="data row284 col3" >Emberling, Defender of Delusions</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col4" class="data row284 col4" >$4.10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col5" class="data row284 col5" >Lisjaskan36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row284_col6" class="data row284 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row285" class="row_heading level0 row285" >285</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col0" class="data row285 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col1" class="data row285 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col2" class="data row285 col2" >78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col3" class="data row285 col3" >Glimmer, Ender of the Moon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col4" class="data row285 col4" >$2.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col5" class="data row285 col5" >Aiduecal76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row285_col6" class="data row285 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row286" class="row_heading level0 row286" >286</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col0" class="data row286 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col1" class="data row286 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col2" class="data row286 col2" >54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col3" class="data row286 col3" >Eternal Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col4" class="data row286 col4" >$3.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col5" class="data row286 col5" >Frichosiala98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row286_col6" class="data row286 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row287" class="row_heading level0 row287" >287</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col0" class="data row287 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col1" class="data row287 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col2" class="data row287 col2" >170</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col3" class="data row287 col3" >Shadowsteel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col4" class="data row287 col4" >$1.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col5" class="data row287 col5" >Deelilsasya30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row287_col6" class="data row287 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row288" class="row_heading level0 row288" >288</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col0" class="data row288 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col1" class="data row288 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col2" class="data row288 col2" >99</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col3" class="data row288 col3" >Expiration, Warscythe Of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col4" class="data row288 col4" >$4.53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col5" class="data row288 col5" >Mindilsa60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row288_col6" class="data row288 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row289" class="row_heading level0 row289" >289</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col0" class="data row289 col0" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col1" class="data row289 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col2" class="data row289 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col3" class="data row289 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col4" class="data row289 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col5" class="data row289 col5" >Iladarla40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row289_col6" class="data row289 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row290" class="row_heading level0 row290" >290</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col0" class="data row290 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col1" class="data row290 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col2" class="data row290 col2" >104</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col3" class="data row290 col3" >Gladiator's Glaive</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col4" class="data row290 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col5" class="data row290 col5" >Chrathybust28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row290_col6" class="data row290 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row291" class="row_heading level0 row291" >291</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col0" class="data row291 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col1" class="data row291 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col2" class="data row291 col2" >53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col3" class="data row291 col3" >Vengeance Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col4" class="data row291 col4" >$3.70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col5" class="data row291 col5" >Yarithsurgue62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row291_col6" class="data row291 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row292" class="row_heading level0 row292" >292</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col0" class="data row292 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col1" class="data row292 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col2" class="data row292 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col3" class="data row292 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col4" class="data row292 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col5" class="data row292 col5" >Lisistaya47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row292_col6" class="data row292 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row293" class="row_heading level0 row293" >293</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col0" class="data row293 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col1" class="data row293 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col2" class="data row293 col2" >95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col3" class="data row293 col3" >Singed Onyx Warscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col4" class="data row293 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col5" class="data row293 col5" >Mindossa76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row293_col6" class="data row293 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row294" class="row_heading level0 row294" >294</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col0" class="data row294 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col1" class="data row294 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col2" class="data row294 col2" >64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col3" class="data row294 col3" >Fusion Pummel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col4" class="data row294 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col5" class="data row294 col5" >Assilsan72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row294_col6" class="data row294 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row295" class="row_heading level0 row295" >295</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col0" class="data row295 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col1" class="data row295 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col2" class="data row295 col2" >135</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col3" class="data row295 col3" >Warped Diamond Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col4" class="data row295 col4" >$4.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col5" class="data row295 col5" >Frichosiala98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row295_col6" class="data row295 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row296" class="row_heading level0 row296" >296</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col0" class="data row296 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col1" class="data row296 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col2" class="data row296 col2" >70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col3" class="data row296 col3" >Hope's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col4" class="data row296 col4" >$3.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col5" class="data row296 col5" >Assassa43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row296_col6" class="data row296 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row297" class="row_heading level0 row297" >297</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col0" class="data row297 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col1" class="data row297 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col2" class="data row297 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col3" class="data row297 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col4" class="data row297 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col5" class="data row297 col5" >Yarolwen77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row297_col6" class="data row297 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row298" class="row_heading level0 row298" >298</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col0" class="data row298 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col1" class="data row298 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col2" class="data row298 col2" >141</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col3" class="data row298 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col4" class="data row298 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col5" class="data row298 col5" >Faralcil63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row298_col6" class="data row298 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row299" class="row_heading level0 row299" >299</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col0" class="data row299 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col1" class="data row299 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col2" class="data row299 col2" >119</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col3" class="data row299 col3" >Stormbringer, Dark Blade of Ending Misery</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col4" class="data row299 col4" >$2.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col5" class="data row299 col5" >Sondilsa40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row299_col6" class="data row299 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row300" class="row_heading level0 row300" >300</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col0" class="data row300 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col1" class="data row300 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col2" class="data row300 col2" >99</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col3" class="data row300 col3" >Expiration, Warscythe Of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col4" class="data row300 col4" >$4.53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col5" class="data row300 col5" >Lisossan98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row300_col6" class="data row300 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row301" class="row_heading level0 row301" >301</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col0" class="data row301 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col1" class="data row301 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col2" class="data row301 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col3" class="data row301 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col4" class="data row301 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col5" class="data row301 col5" >Chadossa89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row301_col6" class="data row301 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row302" class="row_heading level0 row302" >302</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col0" class="data row302 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col1" class="data row302 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col2" class="data row302 col2" >183</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col3" class="data row302 col3" >Dragon's Greatsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col4" class="data row302 col4" >$2.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col5" class="data row302 col5" >Eosrirgue62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row302_col6" class="data row302 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row303" class="row_heading level0 row303" >303</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col0" class="data row303 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col1" class="data row303 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col2" class="data row303 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col3" class="data row303 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col4" class="data row303 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col5" class="data row303 col5" >Lassilsa41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row303_col6" class="data row303 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row304" class="row_heading level0 row304" >304</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col0" class="data row304 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col1" class="data row304 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col2" class="data row304 col2" >173</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col3" class="data row304 col3" >Stormfury Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col4" class="data row304 col4" >$4.83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col5" class="data row304 col5" >Sondastan54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row304_col6" class="data row304 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row305" class="row_heading level0 row305" >305</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col0" class="data row305 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col1" class="data row305 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col2" class="data row305 col2" >98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col3" class="data row305 col3" >Deadline, Voice Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col4" class="data row305 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col5" class="data row305 col5" >Filrion44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row305_col6" class="data row305 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row306" class="row_heading level0 row306" >306</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col0" class="data row306 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col1" class="data row306 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col2" class="data row306 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col3" class="data row306 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col4" class="data row306 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col5" class="data row306 col5" >Lassassasda30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row306_col6" class="data row306 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row307" class="row_heading level0 row307" >307</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col0" class="data row307 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col1" class="data row307 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col2" class="data row307 col2" >180</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col3" class="data row307 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col4" class="data row307 col4" >$2.78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col5" class="data row307 col5" >Aidain51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row307_col6" class="data row307 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row308" class="row_heading level0 row308" >308</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col0" class="data row308 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col1" class="data row308 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col2" class="data row308 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col3" class="data row308 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col4" class="data row308 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col5" class="data row308 col5" >Aduephos78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row308_col6" class="data row308 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row309" class="row_heading level0 row309" >309</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col0" class="data row309 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col1" class="data row309 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col2" class="data row309 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col3" class="data row309 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col4" class="data row309 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col5" class="data row309 col5" >Hainaria90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row309_col6" class="data row309 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row310" class="row_heading level0 row310" >310</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col0" class="data row310 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col1" class="data row310 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col2" class="data row310 col2" >131</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col3" class="data row310 col3" >Fury</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col4" class="data row310 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col5" class="data row310 col5" >Eusri70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row310_col6" class="data row310 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row311" class="row_heading level0 row311" >311</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col0" class="data row311 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col1" class="data row311 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col2" class="data row311 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col3" class="data row311 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col4" class="data row311 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col5" class="data row311 col5" >Raerithsti62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row311_col6" class="data row311 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row312" class="row_heading level0 row312" >312</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col0" class="data row312 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col1" class="data row312 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col2" class="data row312 col2" >68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col3" class="data row312 col3" >Storm-Weaver, Slayer of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col4" class="data row312 col4" >$2.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col5" class="data row312 col5" >Aerithllora36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row312_col6" class="data row312 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row313" class="row_heading level0 row313" >313</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col0" class="data row313 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col1" class="data row313 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col2" class="data row313 col2" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col3" class="data row313 col3" >Curved Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col4" class="data row313 col4" >$1.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col5" class="data row313 col5" >Reuthelis39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row313_col6" class="data row313 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row314" class="row_heading level0 row314" >314</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col0" class="data row314 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col1" class="data row314 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col2" class="data row314 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col3" class="data row314 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col4" class="data row314 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col5" class="data row314 col5" >Sundaststa26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row314_col6" class="data row314 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row315" class="row_heading level0 row315" >315</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col0" class="data row315 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col1" class="data row315 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col2" class="data row315 col2" >54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col3" class="data row315 col3" >Eternal Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col4" class="data row315 col4" >$3.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col5" class="data row315 col5" >Aelin32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row315_col6" class="data row315 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row316" class="row_heading level0 row316" >316</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col0" class="data row316 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col1" class="data row316 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col2" class="data row316 col2" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col3" class="data row316 col3" >Dawne</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col4" class="data row316 col4" >$4.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col5" class="data row316 col5" >Sundadarla27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row316_col6" class="data row316 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row317" class="row_heading level0 row317" >317</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col0" class="data row317 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col1" class="data row317 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col2" class="data row317 col2" >173</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col3" class="data row317 col3" >Stormfury Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col4" class="data row317 col4" >$4.83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col5" class="data row317 col5" >Aeliru63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row317_col6" class="data row317 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row318" class="row_heading level0 row318" >318</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col0" class="data row318 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col1" class="data row318 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col2" class="data row318 col2" >60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col3" class="data row318 col3" >Wolf</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col4" class="data row318 col4" >$1.84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col5" class="data row318 col5" >Mindilsa60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row318_col6" class="data row318 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row319" class="row_heading level0 row319" >319</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col0" class="data row319 col0" >42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col1" class="data row319 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col2" class="data row319 col2" >110</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col3" class="data row319 col3" >Suspension</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col4" class="data row319 col4" >$2.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col5" class="data row319 col5" >Lisista27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row319_col6" class="data row319 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row320" class="row_heading level0 row320" >320</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col0" class="data row320 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col1" class="data row320 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col2" class="data row320 col2" >76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col3" class="data row320 col3" >Haunted Bronzed Bludgeon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col4" class="data row320 col4" >$4.12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col5" class="data row320 col5" >Narirra38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row320_col6" class="data row320 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row321" class="row_heading level0 row321" >321</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col0" class="data row321 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col1" class="data row321 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col2" class="data row321 col2" >137</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col3" class="data row321 col3" >Aetherius, Boon of the Blessed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col4" class="data row321 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col5" class="data row321 col5" >Eustyria89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row321_col6" class="data row321 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row322" class="row_heading level0 row322" >322</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col0" class="data row322 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col1" class="data row322 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col2" class="data row322 col2" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col3" class="data row322 col3" >Chaos, Ender of the End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col4" class="data row322 col4" >$3.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col5" class="data row322 col5" >Phistym51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row322_col6" class="data row322 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row323" class="row_heading level0 row323" >323</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col0" class="data row323 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col1" class="data row323 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col2" class="data row323 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col3" class="data row323 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col4" class="data row323 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col5" class="data row323 col5" >Salilis27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row323_col6" class="data row323 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row324" class="row_heading level0 row324" >324</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col0" class="data row324 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col1" class="data row324 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col2" class="data row324 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col3" class="data row324 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col4" class="data row324 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col5" class="data row324 col5" >Layjask75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row324_col6" class="data row324 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row325" class="row_heading level0 row325" >325</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col0" class="data row325 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col1" class="data row325 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col2" class="data row325 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col3" class="data row325 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col4" class="data row325 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col5" class="data row325 col5" >Tyaeristi78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row325_col6" class="data row325 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row326" class="row_heading level0 row326" >326</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col0" class="data row326 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col1" class="data row326 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col2" class="data row326 col2" >60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col3" class="data row326 col3" >Wolf</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col4" class="data row326 col4" >$1.84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col5" class="data row326 col5" >Lirtyrdesta65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row326_col6" class="data row326 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row327" class="row_heading level0 row327" >327</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col0" class="data row327 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col1" class="data row327 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col2" class="data row327 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col3" class="data row327 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col4" class="data row327 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col5" class="data row327 col5" >Syalollorap93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row327_col6" class="data row327 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row328" class="row_heading level0 row328" >328</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col0" class="data row328 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col1" class="data row328 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col2" class="data row328 col2" >125</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col3" class="data row328 col3" >Whistling Mithril Warblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col4" class="data row328 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col5" class="data row328 col5" >Assylla81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row328_col6" class="data row328 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row329" class="row_heading level0 row329" >329</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col0" class="data row329 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col1" class="data row329 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col2" class="data row329 col2" >61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col3" class="data row329 col3" >Ragnarok</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col4" class="data row329 col4" >$3.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col5" class="data row329 col5" >Eurisuru25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row329_col6" class="data row329 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row330" class="row_heading level0 row330" >330</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col0" class="data row330 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col1" class="data row330 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col2" class="data row330 col2" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col3" class="data row330 col3" >Dawne</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col4" class="data row330 col4" >$4.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col5" class="data row330 col5" >Narirra38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row330_col6" class="data row330 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row331" class="row_heading level0 row331" >331</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col0" class="data row331 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col1" class="data row331 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col2" class="data row331 col2" >70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col3" class="data row331 col3" >Hope's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col4" class="data row331 col4" >$3.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col5" class="data row331 col5" >Mindjasksya61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row331_col6" class="data row331 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row332" class="row_heading level0 row332" >332</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col0" class="data row332 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col1" class="data row332 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col2" class="data row332 col2" >50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col3" class="data row332 col3" >Dawn</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col4" class="data row332 col4" >$2.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col5" class="data row332 col5" >Eusri44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row332_col6" class="data row332 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row333" class="row_heading level0 row333" >333</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col0" class="data row333 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col1" class="data row333 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col2" class="data row333 col2" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col3" class="data row333 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col4" class="data row333 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col5" class="data row333 col5" >Aeliru63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row333_col6" class="data row333 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row334" class="row_heading level0 row334" >334</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col0" class="data row334 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col1" class="data row334 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col2" class="data row334 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col3" class="data row334 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col4" class="data row334 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col5" class="data row334 col5" >Rarith48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row334_col6" class="data row334 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row335" class="row_heading level0 row335" >335</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col0" class="data row335 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col1" class="data row335 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col2" class="data row335 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col3" class="data row335 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col4" class="data row335 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col5" class="data row335 col5" >Yalaeria91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row335_col6" class="data row335 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row336" class="row_heading level0 row336" >336</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col0" class="data row336 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col1" class="data row336 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col2" class="data row336 col2" >173</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col3" class="data row336 col3" >Stormfury Longsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col4" class="data row336 col4" >$4.83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col5" class="data row336 col5" >Iskadarya95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row336_col6" class="data row336 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row337" class="row_heading level0 row337" >337</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col0" class="data row337 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col1" class="data row337 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col2" class="data row337 col2" >140</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col3" class="data row337 col3" >Striker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col4" class="data row337 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col5" class="data row337 col5" >Saedue76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row337_col6" class="data row337 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row338" class="row_heading level0 row338" >338</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col0" class="data row338 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col1" class="data row338 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col2" class="data row338 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col3" class="data row338 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col4" class="data row338 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col5" class="data row338 col5" >Lisossanya98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row338_col6" class="data row338 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row339" class="row_heading level0 row339" >339</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col0" class="data row339 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col1" class="data row339 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col2" class="data row339 col2" >57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col3" class="data row339 col3" >Despair, Favor of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col4" class="data row339 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col5" class="data row339 col5" >Iarithdil76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row339_col6" class="data row339 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row340" class="row_heading level0 row340" >340</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col0" class="data row340 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col1" class="data row340 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col2" class="data row340 col2" >169</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col3" class="data row340 col3" >Interrogator, Blood Blade of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col4" class="data row340 col4" >$3.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col5" class="data row340 col5" >Chanosia60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row340_col6" class="data row340 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row341" class="row_heading level0 row341" >341</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col0" class="data row341 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col1" class="data row341 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col2" class="data row341 col2" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col3" class="data row341 col3" >Thorn, Conqueror of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col4" class="data row341 col4" >$2.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col5" class="data row341 col5" >Aeliriarin93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row341_col6" class="data row341 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row342" class="row_heading level0 row342" >342</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col0" class="data row342 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col1" class="data row342 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col2" class="data row342 col2" >50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col3" class="data row342 col3" >Dawn</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col4" class="data row342 col4" >$2.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col5" class="data row342 col5" >Raedalis34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row342_col6" class="data row342 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row343" class="row_heading level0 row343" >343</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col0" class="data row343 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col1" class="data row343 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col2" class="data row343 col2" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col3" class="data row343 col3" >Curved Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col4" class="data row343 col4" >$1.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col5" class="data row343 col5" >Meosridil82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row343_col6" class="data row343 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row344" class="row_heading level0 row344" >344</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col0" class="data row344 col0" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col1" class="data row344 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col2" class="data row344 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col3" class="data row344 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col4" class="data row344 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col5" class="data row344 col5" >Sondossa55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row344_col6" class="data row344 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row345" class="row_heading level0 row345" >345</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col0" class="data row345 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col1" class="data row345 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col2" class="data row345 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col3" class="data row345 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col4" class="data row345 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col5" class="data row345 col5" >Iadueria43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row345_col6" class="data row345 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row346" class="row_heading level0 row346" >346</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col0" class="data row346 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col1" class="data row346 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col2" class="data row346 col2" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col3" class="data row346 col3" >Possessed Core</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col4" class="data row346 col4" >$1.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col5" class="data row346 col5" >Lisico81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row346_col6" class="data row346 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row347" class="row_heading level0 row347" >347</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col0" class="data row347 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col1" class="data row347 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col2" class="data row347 col2" >146</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col3" class="data row347 col3" >Warped Iron Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col4" class="data row347 col4" >$4.08</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col5" class="data row347 col5" >Ialo60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row347_col6" class="data row347 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row348" class="row_heading level0 row348" >348</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col0" class="data row348 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col1" class="data row348 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col2" class="data row348 col2" >177</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col3" class="data row348 col3" >Winterthorn, Defender of Shifting Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col4" class="data row348 col4" >$4.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col5" class="data row348 col5" >Syathe73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row348_col6" class="data row348 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row349" class="row_heading level0 row349" >349</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col0" class="data row349 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col1" class="data row349 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col2" class="data row349 col2" >166</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col3" class="data row349 col3" >Thirsty Iron Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col4" class="data row349 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col5" class="data row349 col5" >Lisassa26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row349_col6" class="data row349 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row350" class="row_heading level0 row350" >350</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col0" class="data row350 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col1" class="data row350 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col2" class="data row350 col2" >93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col3" class="data row350 col3" >Apocalyptic Battlescythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col4" class="data row350 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col5" class="data row350 col5" >Rasrirgue43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row350_col6" class="data row350 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row351" class="row_heading level0 row351" >351</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col0" class="data row351 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col1" class="data row351 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col2" class="data row351 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col3" class="data row351 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col4" class="data row351 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col5" class="data row351 col5" >Aerillorin70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row351_col6" class="data row351 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row352" class="row_heading level0 row352" >352</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col0" class="data row352 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col1" class="data row352 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col2" class="data row352 col2" >56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col3" class="data row352 col3" >Foul Titanium Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col4" class="data row352 col4" >$4.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col5" class="data row352 col5" >Quelatarn54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row352_col6" class="data row352 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row353" class="row_heading level0 row353" >353</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col0" class="data row353 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col1" class="data row353 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col2" class="data row353 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col3" class="data row353 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col4" class="data row353 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col5" class="data row353 col5" >Airithrin43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row353_col6" class="data row353 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row354" class="row_heading level0 row354" >354</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col0" class="data row354 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col1" class="data row354 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col2" class="data row354 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col3" class="data row354 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col4" class="data row354 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col5" class="data row354 col5" >Mindirra92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row354_col6" class="data row354 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row355" class="row_heading level0 row355" >355</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col0" class="data row355 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col1" class="data row355 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col2" class="data row355 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col3" class="data row355 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col4" class="data row355 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col5" class="data row355 col5" >Lisjasksda68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row355_col6" class="data row355 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row356" class="row_heading level0 row356" >356</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col0" class="data row356 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col1" class="data row356 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col2" class="data row356 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col3" class="data row356 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col4" class="data row356 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col5" class="data row356 col5" >Aerithnuphos61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row356_col6" class="data row356 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row357" class="row_heading level0 row357" >357</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col0" class="data row357 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col1" class="data row357 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col2" class="data row357 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col3" class="data row357 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col4" class="data row357 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col5" class="data row357 col5" >Sundast29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row357_col6" class="data row357 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row358" class="row_heading level0 row358" >358</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col0" class="data row358 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col1" class="data row358 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col2" class="data row358 col2" >87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col3" class="data row358 col3" >Deluge, Edge of the West</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col4" class="data row358 col4" >$2.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col5" class="data row358 col5" >Lirtosia72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row358_col6" class="data row358 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row359" class="row_heading level0 row359" >359</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col0" class="data row359 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col1" class="data row359 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col2" class="data row359 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col3" class="data row359 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col4" class="data row359 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col5" class="data row359 col5" >Aeliriam77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row359_col6" class="data row359 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row360" class="row_heading level0 row360" >360</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col0" class="data row360 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col1" class="data row360 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col2" class="data row360 col2" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col3" class="data row360 col3" >Souleater</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col4" class="data row360 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col5" class="data row360 col5" >Lisirra55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row360_col6" class="data row360 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row361" class="row_heading level0 row361" >361</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col0" class="data row361 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col1" class="data row361 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col2" class="data row361 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col3" class="data row361 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col4" class="data row361 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col5" class="data row361 col5" >Aeral97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row361_col6" class="data row361 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row362" class="row_heading level0 row362" >362</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col0" class="data row362 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col1" class="data row362 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col2" class="data row362 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col3" class="data row362 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col4" class="data row362 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col5" class="data row362 col5" >Lisosiast26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row362_col6" class="data row362 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row363" class="row_heading level0 row363" >363</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col0" class="data row363 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col1" class="data row363 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col2" class="data row363 col2" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col3" class="data row363 col3" >Restored Bauble</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col4" class="data row363 col4" >$3.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col5" class="data row363 col5" >Yathecal72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row363_col6" class="data row363 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row364" class="row_heading level0 row364" >364</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col0" class="data row364 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col1" class="data row364 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col2" class="data row364 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col3" class="data row364 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col4" class="data row364 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col5" class="data row364 col5" >Lirtistasta79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row364_col6" class="data row364 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row365" class="row_heading level0 row365" >365</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col0" class="data row365 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col1" class="data row365 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col2" class="data row365 col2" >67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col3" class="data row365 col3" >Celeste, Incarnation of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col4" class="data row365 col4" >$2.31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col5" class="data row365 col5" >Lisadar44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row365_col6" class="data row365 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row366" class="row_heading level0 row366" >366</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col0" class="data row366 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col1" class="data row366 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col2" class="data row366 col2" >133</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col3" class="data row366 col3" >Faith's Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col4" class="data row366 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col5" class="data row366 col5" >Jiskossa51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row366_col6" class="data row366 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row367" class="row_heading level0 row367" >367</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col0" class="data row367 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col1" class="data row367 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col2" class="data row367 col2" >100</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col3" class="data row367 col3" >Blindscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col4" class="data row367 col4" >$3.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col5" class="data row367 col5" >Qilatie51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row367_col6" class="data row367 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row368" class="row_heading level0 row368" >368</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col0" class="data row368 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col1" class="data row368 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col2" class="data row368 col2" >153</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col3" class="data row368 col3" >Mercenary Sabre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col4" class="data row368 col4" >$4.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col5" class="data row368 col5" >Eusri70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row368_col6" class="data row368 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row369" class="row_heading level0 row369" >369</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col0" class="data row369 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col1" class="data row369 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col2" class="data row369 col2" >118</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col3" class="data row369 col3" >Ghost Reaver, Longsword of Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col4" class="data row369 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col5" class="data row369 col5" >Isurria36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row369_col6" class="data row369 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row370" class="row_heading level0 row370" >370</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col0" class="data row370 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col1" class="data row370 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col2" class="data row370 col2" >151</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col3" class="data row370 col3" >Severance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col4" class="data row370 col4" >$1.85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col5" class="data row370 col5" >Sundastnya66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row370_col6" class="data row370 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row371" class="row_heading level0 row371" >371</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col0" class="data row371 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col1" class="data row371 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col2" class="data row371 col2" >81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col3" class="data row371 col3" >Dreamkiss</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col4" class="data row371 col4" >$4.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col5" class="data row371 col5" >Raesursurap33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row371_col6" class="data row371 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row372" class="row_heading level0 row372" >372</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col0" class="data row372 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col1" class="data row372 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col2" class="data row372 col2" >94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col3" class="data row372 col3" >Mourning Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col4" class="data row372 col4" >$1.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col5" class="data row372 col5" >Sondassasya91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row372_col6" class="data row372 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row373" class="row_heading level0 row373" >373</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col0" class="data row373 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col1" class="data row373 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col2" class="data row373 col2" >114</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col3" class="data row373 col3" >Yearning Mageblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col4" class="data row373 col4" >$1.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col5" class="data row373 col5" >Ermol76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row373_col6" class="data row373 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row374" class="row_heading level0 row374" >374</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col0" class="data row374 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col1" class="data row374 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col2" class="data row374 col2" >77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col3" class="data row374 col3" >Piety, Guardian of Riddles</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col4" class="data row374 col4" >$3.68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col5" class="data row374 col5" >Eosurdru76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row374_col6" class="data row374 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row375" class="row_heading level0 row375" >375</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col0" class="data row375 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col1" class="data row375 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col2" class="data row375 col2" >42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col3" class="data row375 col3" >The Decapitator</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col4" class="data row375 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col5" class="data row375 col5" >Yadaisuir65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row375_col6" class="data row375 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row376" class="row_heading level0 row376" >376</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col0" class="data row376 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col1" class="data row376 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col2" class="data row376 col2" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col3" class="data row376 col3" >Curved Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col4" class="data row376 col4" >$1.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col5" class="data row376 col5" >Zhisrisu83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row376_col6" class="data row376 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row377" class="row_heading level0 row377" >377</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col0" class="data row377 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col1" class="data row377 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col2" class="data row377 col2" >174</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col3" class="data row377 col3" >Primitive Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col4" class="data row377 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col5" class="data row377 col5" >Aduephos78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row377_col6" class="data row377 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row378" class="row_heading level0 row378" >378</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col0" class="data row378 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col1" class="data row378 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col2" class="data row378 col2" >69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col3" class="data row378 col3" >Frenzy, Defender of the Harvest</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col4" class="data row378 col4" >$1.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col5" class="data row378 col5" >Sondassa68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row378_col6" class="data row378 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row379" class="row_heading level0 row379" >379</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col0" class="data row379 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col1" class="data row379 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col2" class="data row379 col2" >141</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col3" class="data row379 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col4" class="data row379 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col5" class="data row379 col5" >Chamirraya83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row379_col6" class="data row379 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row380" class="row_heading level0 row380" >380</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col0" class="data row380 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col1" class="data row380 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col2" class="data row380 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col3" class="data row380 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col4" class="data row380 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col5" class="data row380 col5" >Alaephos75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row380_col6" class="data row380 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row381" class="row_heading level0 row381" >381</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col0" class="data row381 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col1" class="data row381 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col2" class="data row381 col2" >166</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col3" class="data row381 col3" >Thirsty Iron Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col4" class="data row381 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col5" class="data row381 col5" >Haellysu29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row381_col6" class="data row381 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row382" class="row_heading level0 row382" >382</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col0" class="data row382 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col1" class="data row382 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col2" class="data row382 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col3" class="data row382 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col4" class="data row382 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col5" class="data row382 col5" >Yarithphos28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row382_col6" class="data row382 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row383" class="row_heading level0 row383" >383</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col0" class="data row383 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col1" class="data row383 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col2" class="data row383 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col3" class="data row383 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col4" class="data row383 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col5" class="data row383 col5" >Ingatcil75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row383_col6" class="data row383 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row384" class="row_heading level0 row384" >384</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col0" class="data row384 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col1" class="data row384 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col2" class="data row384 col2" >143</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col3" class="data row384 col3" >Frenzied Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col4" class="data row384 col4" >$2.60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col5" class="data row384 col5" >Eothe56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row384_col6" class="data row384 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row385" class="row_heading level0 row385" >385</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col0" class="data row385 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col1" class="data row385 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col2" class="data row385 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col3" class="data row385 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col4" class="data row385 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col5" class="data row385 col5" >Haerith37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row385_col6" class="data row385 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row386" class="row_heading level0 row386" >386</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col0" class="data row386 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col1" class="data row386 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col2" class="data row386 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col3" class="data row386 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col4" class="data row386 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col5" class="data row386 col5" >Assithasta65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row386_col6" class="data row386 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row387" class="row_heading level0 row387" >387</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col0" class="data row387 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col1" class="data row387 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col2" class="data row387 col2" >51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col3" class="data row387 col3" >Endbringer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col4" class="data row387 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col5" class="data row387 col5" >Ethruard50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row387_col6" class="data row387 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row388" class="row_heading level0 row388" >388</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col0" class="data row388 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col1" class="data row388 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col2" class="data row388 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col3" class="data row388 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col4" class="data row388 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col5" class="data row388 col5" >Palurrian69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row388_col6" class="data row388 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row389" class="row_heading level0 row389" >389</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col0" class="data row389 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col1" class="data row389 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col2" class="data row389 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col3" class="data row389 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col4" class="data row389 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col5" class="data row389 col5" >Iskistasda86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row389_col6" class="data row389 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row390" class="row_heading level0 row390" >390</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col0" class="data row390 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col1" class="data row390 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col2" class="data row390 col2" >86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col3" class="data row390 col3" >Stormfury Lantern</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col4" class="data row390 col4" >$1.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col5" class="data row390 col5" >Tyaili86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row390_col6" class="data row390 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row391" class="row_heading level0 row391" >391</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col0" class="data row391 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col1" class="data row391 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col2" class="data row391 col2" >141</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col3" class="data row391 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col4" class="data row391 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col5" class="data row391 col5" >Liawista80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row391_col6" class="data row391 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row392" class="row_heading level0 row392" >392</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col0" class="data row392 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col1" class="data row392 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col2" class="data row392 col2" >159</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col3" class="data row392 col3" >Oathbreaker, Spellblade of Trials</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col4" class="data row392 col4" >$3.01</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col5" class="data row392 col5" >Seosri62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row392_col6" class="data row392 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row393" class="row_heading level0 row393" >393</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col0" class="data row393 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col1" class="data row393 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col2" class="data row393 col2" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col3" class="data row393 col3" >Restored Bauble</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col4" class="data row393 col4" >$3.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col5" class="data row393 col5" >Silinu63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row393_col6" class="data row393 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row394" class="row_heading level0 row394" >394</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col0" class="data row394 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col1" class="data row394 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col2" class="data row394 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col3" class="data row394 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col4" class="data row394 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col5" class="data row394 col5" >Aela49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row394_col6" class="data row394 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row395" class="row_heading level0 row395" >395</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col0" class="data row395 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col1" class="data row395 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col2" class="data row395 col2" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col3" class="data row395 col3" >The Void, Vengeance of Dark Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col4" class="data row395 col4" >$2.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col5" class="data row395 col5" >Assosiasta83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row395_col6" class="data row395 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row396" class="row_heading level0 row396" >396</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col0" class="data row396 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col1" class="data row396 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col2" class="data row396 col2" >77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col3" class="data row396 col3" >Piety, Guardian of Riddles</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col4" class="data row396 col4" >$3.68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col5" class="data row396 col5" >Saelollop56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row396_col6" class="data row396 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row397" class="row_heading level0 row397" >397</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col0" class="data row397 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col1" class="data row397 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col2" class="data row397 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col3" class="data row397 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col4" class="data row397 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col5" class="data row397 col5" >Saena74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row397_col6" class="data row397 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row398" class="row_heading level0 row398" >398</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col0" class="data row398 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col1" class="data row398 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col2" class="data row398 col2" >96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col3" class="data row398 col3" >Blood-Forged Skeletal Spine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col4" class="data row398 col4" >$4.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col5" class="data row398 col5" >Tyaelistidru84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row398_col6" class="data row398 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row399" class="row_heading level0 row399" >399</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col0" class="data row399 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col1" class="data row399 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col2" class="data row399 col2" >82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col3" class="data row399 col3" >Nirvana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col4" class="data row399 col4" >$1.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col5" class="data row399 col5" >Chamirrasya33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row399_col6" class="data row399 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row400" class="row_heading level0 row400" >400</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col0" class="data row400 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col1" class="data row400 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col2" class="data row400 col2" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col3" class="data row400 col3" >Riddle, Tribute of Ended Dreams</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col4" class="data row400 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col5" class="data row400 col5" >Smecherdi88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row400_col6" class="data row400 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row401" class="row_heading level0 row401" >401</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col0" class="data row401 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col1" class="data row401 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col2" class="data row401 col2" >121</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col3" class="data row401 col3" >Massacre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col4" class="data row401 col4" >$3.42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col5" class="data row401 col5" >Leulaesti78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row401_col6" class="data row401 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row402" class="row_heading level0 row402" >402</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col0" class="data row402 col0" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col1" class="data row402 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col2" class="data row402 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col3" class="data row402 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col4" class="data row402 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col5" class="data row402 col5" >Tyaenasti87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row402_col6" class="data row402 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row403" class="row_heading level0 row403" >403</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col0" class="data row403 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col1" class="data row403 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col2" class="data row403 col2" >113</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col3" class="data row403 col3" >Solitude's Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col4" class="data row403 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col5" class="data row403 col5" >Sondassa48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row403_col6" class="data row403 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row404" class="row_heading level0 row404" >404</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col0" class="data row404 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col1" class="data row404 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col2" class="data row404 col2" >46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col3" class="data row404 col3" >Hopeless Ebon Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col4" class="data row404 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col5" class="data row404 col5" >Deural48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row404_col6" class="data row404 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row405" class="row_heading level0 row405" >405</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col0" class="data row405 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col1" class="data row405 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col2" class="data row405 col2" >76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col3" class="data row405 col3" >Haunted Bronzed Bludgeon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col4" class="data row405 col4" >$4.12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col5" class="data row405 col5" >Saistydru69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row405_col6" class="data row405 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row406" class="row_heading level0 row406" >406</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col0" class="data row406 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col1" class="data row406 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col2" class="data row406 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col3" class="data row406 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col4" class="data row406 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col5" class="data row406 col5" >Chamosia29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row406_col6" class="data row406 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row407" class="row_heading level0 row407" >407</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col0" class="data row407 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col1" class="data row407 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col2" class="data row407 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col3" class="data row407 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col4" class="data row407 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col5" class="data row407 col5" >Saisrilis27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row407_col6" class="data row407 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row408" class="row_heading level0 row408" >408</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col0" class="data row408 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col1" class="data row408 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col2" class="data row408 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col3" class="data row408 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col4" class="data row408 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col5" class="data row408 col5" >Indonmol95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row408_col6" class="data row408 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row409" class="row_heading level0 row409" >409</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col0" class="data row409 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col1" class="data row409 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col2" class="data row409 col2" >45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col3" class="data row409 col3" >Glinting Glass Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col4" class="data row409 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col5" class="data row409 col5" >Fironon91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row409_col6" class="data row409 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row410" class="row_heading level0 row410" >410</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col0" class="data row410 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col1" class="data row410 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col2" class="data row410 col2" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col3" class="data row410 col3" >Riddle, Tribute of Ended Dreams</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col4" class="data row410 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col5" class="data row410 col5" >Ryanara76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row410_col6" class="data row410 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row411" class="row_heading level0 row411" >411</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col0" class="data row411 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col1" class="data row411 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col2" class="data row411 col2" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col3" class="data row411 col3" >Thorn, Satchel of Dark Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col4" class="data row411 col4" >$4.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col5" class="data row411 col5" >Saedue76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row411_col6" class="data row411 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row412" class="row_heading level0 row412" >412</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col0" class="data row412 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col1" class="data row412 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col2" class="data row412 col2" >114</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col3" class="data row412 col3" >Yearning Mageblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col4" class="data row412 col4" >$1.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col5" class="data row412 col5" >Lirtossanya27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row412_col6" class="data row412 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row413" class="row_heading level0 row413" >413</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col0" class="data row413 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col1" class="data row413 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col2" class="data row413 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col3" class="data row413 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col4" class="data row413 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col5" class="data row413 col5" >Sondadar26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row413_col6" class="data row413 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row414" class="row_heading level0 row414" >414</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col0" class="data row414 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col1" class="data row414 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col2" class="data row414 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col3" class="data row414 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col4" class="data row414 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col5" class="data row414 col5" >Phalinun47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row414_col6" class="data row414 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row415" class="row_heading level0 row415" >415</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col0" class="data row415 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col1" class="data row415 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col2" class="data row415 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col3" class="data row415 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col4" class="data row415 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col5" class="data row415 col5" >Chamistast30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row415_col6" class="data row415 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row416" class="row_heading level0 row416" >416</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col0" class="data row416 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col1" class="data row416 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col2" class="data row416 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col3" class="data row416 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col4" class="data row416 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col5" class="data row416 col5" >Hiarideu73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row416_col6" class="data row416 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row417" class="row_heading level0 row417" >417</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col0" class="data row417 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col1" class="data row417 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col2" class="data row417 col2" >119</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col3" class="data row417 col3" >Stormbringer, Dark Blade of Ending Misery</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col4" class="data row417 col4" >$2.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col5" class="data row417 col5" >Qilunan34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row417_col6" class="data row417 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row418" class="row_heading level0 row418" >418</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col0" class="data row418 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col1" class="data row418 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col2" class="data row418 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col3" class="data row418 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col4" class="data row418 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col5" class="data row418 col5" >Pharithdil38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row418_col6" class="data row418 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row419" class="row_heading level0 row419" >419</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col0" class="data row419 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col1" class="data row419 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col2" class="data row419 col2" >42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col3" class="data row419 col3" >The Decapitator</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col4" class="data row419 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col5" class="data row419 col5" >Tyeuladeu30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row419_col6" class="data row419 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row420" class="row_heading level0 row420" >420</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col0" class="data row420 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col1" class="data row420 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col2" class="data row420 col2" >170</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col3" class="data row420 col3" >Shadowsteel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col4" class="data row420 col4" >$1.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col5" class="data row420 col5" >Sondastan54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row420_col6" class="data row420 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row421" class="row_heading level0 row421" >421</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col0" class="data row421 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col1" class="data row421 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col2" class="data row421 col2" >150</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col3" class="data row421 col3" >Deathraze</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col4" class="data row421 col4" >$4.54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col5" class="data row421 col5" >Ina92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row421_col6" class="data row421 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row422" class="row_heading level0 row422" >422</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col0" class="data row422 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col1" class="data row422 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col2" class="data row422 col2" >164</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col3" class="data row422 col3" >Exiled Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col4" class="data row422 col4" >$1.92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col5" class="data row422 col5" >Saida58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row422_col6" class="data row422 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row423" class="row_heading level0 row423" >423</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col0" class="data row423 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col1" class="data row423 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col2" class="data row423 col2" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col3" class="data row423 col3" >Chaos, Ender of the End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col4" class="data row423 col4" >$3.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col5" class="data row423 col5" >Aithelis62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row423_col6" class="data row423 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row424" class="row_heading level0 row424" >424</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col0" class="data row424 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col1" class="data row424 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col2" class="data row424 col2" >139</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col3" class="data row424 col3" >Mercy, Katana of Dismay</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col4" class="data row424 col4" >$4.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col5" class="data row424 col5" >Indcil77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row424_col6" class="data row424 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row425" class="row_heading level0 row425" >425</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col0" class="data row425 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col1" class="data row425 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col2" class="data row425 col2" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col3" class="data row425 col3" >Possessed Core</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col4" class="data row425 col4" >$1.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col5" class="data row425 col5" >Hallysucal81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row425_col6" class="data row425 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row426" class="row_heading level0 row426" >426</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col0" class="data row426 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col1" class="data row426 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col2" class="data row426 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col3" class="data row426 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col4" class="data row426 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col5" class="data row426 col5" >Tyeuduephos81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row426_col6" class="data row426 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row427" class="row_heading level0 row427" >427</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col0" class="data row427 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col1" class="data row427 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col2" class="data row427 col2" >131</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col3" class="data row427 col3" >Fury</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col4" class="data row427 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col5" class="data row427 col5" >Heosrisuir72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row427_col6" class="data row427 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row428" class="row_heading level0 row428" >428</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col0" class="data row428 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col1" class="data row428 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col2" class="data row428 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col3" class="data row428 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col4" class="data row428 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col5" class="data row428 col5" >Chadossa56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row428_col6" class="data row428 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row429" class="row_heading level0 row429" >429</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col0" class="data row429 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col1" class="data row429 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col2" class="data row429 col2" >82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col3" class="data row429 col3" >Nirvana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col4" class="data row429 col4" >$1.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col5" class="data row429 col5" >Hailaphos89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row429_col6" class="data row429 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row430" class="row_heading level0 row430" >430</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col0" class="data row430 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col1" class="data row430 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col2" class="data row430 col2" >74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col3" class="data row430 col3" >Yearning Crusher</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col4" class="data row430 col4" >$1.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col5" class="data row430 col5" >Lirtassa47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row430_col6" class="data row430 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row431" class="row_heading level0 row431" >431</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col0" class="data row431 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col1" class="data row431 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col2" class="data row431 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col3" class="data row431 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col4" class="data row431 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col5" class="data row431 col5" >Aduephos78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row431_col6" class="data row431 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row432" class="row_heading level0 row432" >432</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col0" class="data row432 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col1" class="data row432 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col2" class="data row432 col2" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col3" class="data row432 col3" >Netherbane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col4" class="data row432 col4" >$1.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col5" class="data row432 col5" >Sondilsa40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row432_col6" class="data row432 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row433" class="row_heading level0 row433" >433</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col0" class="data row433 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col1" class="data row433 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col2" class="data row433 col2" >180</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col3" class="data row433 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col4" class="data row433 col4" >$2.78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col5" class="data row433 col5" >Ithesuphos68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row433_col6" class="data row433 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row434" class="row_heading level0 row434" >434</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col0" class="data row434 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col1" class="data row434 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col2" class="data row434 col2" >98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col3" class="data row434 col3" >Deadline, Voice Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col4" class="data row434 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col5" class="data row434 col5" >Eula35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row434_col6" class="data row434 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row435" class="row_heading level0 row435" >435</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col0" class="data row435 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col1" class="data row435 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col2" class="data row435 col2" >159</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col3" class="data row435 col3" >Oathbreaker, Spellblade of Trials</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col4" class="data row435 col4" >$3.01</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col5" class="data row435 col5" >Aina42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row435_col6" class="data row435 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row436" class="row_heading level0 row436" >436</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col0" class="data row436 col0" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col1" class="data row436 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col2" class="data row436 col2" >131</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col3" class="data row436 col3" >Fury</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col4" class="data row436 col4" >$4.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col5" class="data row436 col5" >Ethrusuard41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row436_col6" class="data row436 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row437" class="row_heading level0 row437" >437</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col0" class="data row437 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col1" class="data row437 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col2" class="data row437 col2" >82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col3" class="data row437 col3" >Nirvana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col4" class="data row437 col4" >$1.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col5" class="data row437 col5" >Zhisrisu83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row437_col6" class="data row437 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row438" class="row_heading level0 row438" >438</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col0" class="data row438 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col1" class="data row438 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col2" class="data row438 col2" >111</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col3" class="data row438 col3" >Misery's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col4" class="data row438 col4" >$2.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col5" class="data row438 col5" >Isursti83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row438_col6" class="data row438 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row439" class="row_heading level0 row439" >439</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col0" class="data row439 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col1" class="data row439 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col2" class="data row439 col2" >41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col3" class="data row439 col3" >Orbit</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col4" class="data row439 col4" >$1.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col5" class="data row439 col5" >Chanirrasta87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row439_col6" class="data row439 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row440" class="row_heading level0 row440" >440</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col0" class="data row440 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col1" class="data row440 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col2" class="data row440 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col3" class="data row440 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col4" class="data row440 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col5" class="data row440 col5" >Stryanastip77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row440_col6" class="data row440 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row441" class="row_heading level0 row441" >441</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col0" class="data row441 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col1" class="data row441 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col2" class="data row441 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col3" class="data row441 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col4" class="data row441 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col5" class="data row441 col5" >Ilirrasda54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row441_col6" class="data row441 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row442" class="row_heading level0 row442" >442</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col0" class="data row442 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col1" class="data row442 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col2" class="data row442 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col3" class="data row442 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col4" class="data row442 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col5" class="data row442 col5" >Liri91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row442_col6" class="data row442 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row443" class="row_heading level0 row443" >443</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col0" class="data row443 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col1" class="data row443 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col2" class="data row443 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col3" class="data row443 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col4" class="data row443 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col5" class="data row443 col5" >Undadar97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row443_col6" class="data row443 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row444" class="row_heading level0 row444" >444</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col0" class="data row444 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col1" class="data row444 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col2" class="data row444 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col3" class="data row444 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col4" class="data row444 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col5" class="data row444 col5" >Ithergue48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row444_col6" class="data row444 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row445" class="row_heading level0 row445" >445</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col0" class="data row445 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col1" class="data row445 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col2" class="data row445 col2" >95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col3" class="data row445 col3" >Singed Onyx Warscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col4" class="data row445 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col5" class="data row445 col5" >Saistyphos30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row445_col6" class="data row445 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row446" class="row_heading level0 row446" >446</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col0" class="data row446 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col1" class="data row446 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col2" class="data row446 col2" >47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col3" class="data row446 col3" >Alpha, Reach of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col4" class="data row446 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col5" class="data row446 col5" >Lisosianya62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row446_col6" class="data row446 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row447" class="row_heading level0 row447" >447</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col0" class="data row447 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col1" class="data row447 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col2" class="data row447 col2" >6</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col3" class="data row447 col3" >Rusty Skull</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col4" class="data row447 col4" >$1.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col5" class="data row447 col5" >Tyaelistidru84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row447_col6" class="data row447 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row448" class="row_heading level0 row448" >448</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col0" class="data row448 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col1" class="data row448 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col2" class="data row448 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col3" class="data row448 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col4" class="data row448 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col5" class="data row448 col5" >Sausosia74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row448_col6" class="data row448 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row449" class="row_heading level0 row449" >449</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col0" class="data row449 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col1" class="data row449 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col2" class="data row449 col2" >123</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col3" class="data row449 col3" >Twilight's Carver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col4" class="data row449 col4" >$1.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col5" class="data row449 col5" >Frichosiala98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row449_col6" class="data row449 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row450" class="row_heading level0 row450" >450</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col0" class="data row450 col0" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col1" class="data row450 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col2" class="data row450 col2" >140</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col3" class="data row450 col3" >Striker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col4" class="data row450 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col5" class="data row450 col5" >Mindimnya67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row450_col6" class="data row450 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row451" class="row_heading level0 row451" >451</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col0" class="data row451 col0" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col1" class="data row451 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col2" class="data row451 col2" >163</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col3" class="data row451 col3" >Thunderfury Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col4" class="data row451 col4" >$3.02</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col5" class="data row451 col5" >Undistasta86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row451_col6" class="data row451 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row452" class="row_heading level0 row452" >452</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col0" class="data row452 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col1" class="data row452 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col2" class="data row452 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col3" class="data row452 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col4" class="data row452 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col5" class="data row452 col5" >Lirtistasta79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row452_col6" class="data row452 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row453" class="row_heading level0 row453" >453</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col0" class="data row453 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col1" class="data row453 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col2" class="data row453 col2" >95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col3" class="data row453 col3" >Singed Onyx Warscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col4" class="data row453 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col5" class="data row453 col5" >Alaesu91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row453_col6" class="data row453 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row454" class="row_heading level0 row454" >454</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col0" class="data row454 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col1" class="data row454 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col2" class="data row454 col2" >100</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col3" class="data row454 col3" >Blindscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col4" class="data row454 col4" >$3.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col5" class="data row454 col5" >Jiskosiala43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row454_col6" class="data row454 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row455" class="row_heading level0 row455" >455</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col0" class="data row455 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col1" class="data row455 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col2" class="data row455 col2" >137</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col3" class="data row455 col3" >Aetherius, Boon of the Blessed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col4" class="data row455 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col5" class="data row455 col5" >Heuralsti66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row455_col6" class="data row455 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row456" class="row_heading level0 row456" >456</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col0" class="data row456 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col1" class="data row456 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col2" class="data row456 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col3" class="data row456 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col4" class="data row456 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col5" class="data row456 col5" >Umuard36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row456_col6" class="data row456 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row457" class="row_heading level0 row457" >457</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col0" class="data row457 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col1" class="data row457 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col2" class="data row457 col2" >68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col3" class="data row457 col3" >Storm-Weaver, Slayer of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col4" class="data row457 col4" >$2.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col5" class="data row457 col5" >Asur53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row457_col6" class="data row457 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row458" class="row_heading level0 row458" >458</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col0" class="data row458 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col1" class="data row458 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col2" class="data row458 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col3" class="data row458 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col4" class="data row458 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col5" class="data row458 col5" >Jiskassa76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row458_col6" class="data row458 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row459" class="row_heading level0 row459" >459</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col0" class="data row459 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col1" class="data row459 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col2" class="data row459 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col3" class="data row459 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col4" class="data row459 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col5" class="data row459 col5" >Thryallym62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row459_col6" class="data row459 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row460" class="row_heading level0 row460" >460</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col0" class="data row460 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col1" class="data row460 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col2" class="data row460 col2" >5</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col3" class="data row460 col3" >Putrid Fan</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col4" class="data row460 col4" >$1.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col5" class="data row460 col5" >Raesty92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row460_col6" class="data row460 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row461" class="row_heading level0 row461" >461</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col0" class="data row461 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col1" class="data row461 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col2" class="data row461 col2" >69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col3" class="data row461 col3" >Frenzy, Defender of the Harvest</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col4" class="data row461 col4" >$1.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col5" class="data row461 col5" >Frichassala85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row461_col6" class="data row461 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row462" class="row_heading level0 row462" >462</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col0" class="data row462 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col1" class="data row462 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col2" class="data row462 col2" >90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col3" class="data row462 col3" >Betrayer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col4" class="data row462 col4" >$1.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col5" class="data row462 col5" >Chamilsan75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row462_col6" class="data row462 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row463" class="row_heading level0 row463" >463</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col0" class="data row463 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col1" class="data row463 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col2" class="data row463 col2" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col3" class="data row463 col3" >The Void, Vengeance of Dark Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col4" class="data row463 col4" >$2.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col5" class="data row463 col5" >Ilosu82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row463_col6" class="data row463 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row464" class="row_heading level0 row464" >464</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col0" class="data row464 col0" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col1" class="data row464 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col2" class="data row464 col2" >163</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col3" class="data row464 col3" >Thunderfury Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col4" class="data row464 col4" >$3.02</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col5" class="data row464 col5" >Mindimnya67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row464_col6" class="data row464 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row465" class="row_heading level0 row465" >465</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col0" class="data row465 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col1" class="data row465 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col2" class="data row465 col2" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col3" class="data row465 col3" >Netherbane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col4" class="data row465 col4" >$1.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col5" class="data row465 col5" >Pheodai94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row465_col6" class="data row465 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row466" class="row_heading level0 row466" >466</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col0" class="data row466 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col1" class="data row466 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col2" class="data row466 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col3" class="data row466 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col4" class="data row466 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col5" class="data row466 col5" >Raerithsti62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row466_col6" class="data row466 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row467" class="row_heading level0 row467" >467</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col0" class="data row467 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col1" class="data row467 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col2" class="data row467 col2" >41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col3" class="data row467 col3" >Orbit</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col4" class="data row467 col4" >$1.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col5" class="data row467 col5" >Undirrasta74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row467_col6" class="data row467 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row468" class="row_heading level0 row468" >468</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col0" class="data row468 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col1" class="data row468 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col2" class="data row468 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col3" class="data row468 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col4" class="data row468 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col5" class="data row468 col5" >Hiasur92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row468_col6" class="data row468 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row469" class="row_heading level0 row469" >469</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col0" class="data row469 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col1" class="data row469 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col2" class="data row469 col2" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col3" class="data row469 col3" >Pursuit, Cudgel of Necromancy</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col4" class="data row469 col4" >$3.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col5" class="data row469 col5" >Tillyrin30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row469_col6" class="data row469 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row470" class="row_heading level0 row470" >470</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col0" class="data row470 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col1" class="data row470 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col2" class="data row470 col2" >134</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col3" class="data row470 col3" >Undead Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col4" class="data row470 col4" >$4.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col5" class="data row470 col5" >Riralsti91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row470_col6" class="data row470 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row471" class="row_heading level0 row471" >471</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col0" class="data row471 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col1" class="data row471 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col2" class="data row471 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col3" class="data row471 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col4" class="data row471 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col5" class="data row471 col5" >Iasur80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row471_col6" class="data row471 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row472" class="row_heading level0 row472" >472</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col0" class="data row472 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col1" class="data row472 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col2" class="data row472 col2" >110</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col3" class="data row472 col3" >Suspension</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col4" class="data row472 col4" >$2.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col5" class="data row472 col5" >Eryon48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row472_col6" class="data row472 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row473" class="row_heading level0 row473" >473</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col0" class="data row473 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col1" class="data row473 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col2" class="data row473 col2" >146</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col3" class="data row473 col3" >Warped Iron Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col4" class="data row473 col4" >$4.08</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col5" class="data row473 col5" >Whaestysu86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row473_col6" class="data row473 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row474" class="row_heading level0 row474" >474</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col0" class="data row474 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col1" class="data row474 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col2" class="data row474 col2" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col3" class="data row474 col3" >Heartless Bone Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col4" class="data row474 col4" >$2.63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col5" class="data row474 col5" >Aiduesu83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row474_col6" class="data row474 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row475" class="row_heading level0 row475" >475</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col0" class="data row475 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col1" class="data row475 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col2" class="data row475 col2" >105</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col3" class="data row475 col3" >Hailstorm Shadowsteel Scythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col4" class="data row475 col4" >$3.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col5" class="data row475 col5" >Iaralsuir44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row475_col6" class="data row475 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row476" class="row_heading level0 row476" >476</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col0" class="data row476 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col1" class="data row476 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col2" class="data row476 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col3" class="data row476 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col4" class="data row476 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col5" class="data row476 col5" >Chanjask65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row476_col6" class="data row476 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row477" class="row_heading level0 row477" >477</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col0" class="data row477 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col1" class="data row477 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col2" class="data row477 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col3" class="data row477 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col4" class="data row477 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col5" class="data row477 col5" >Frichistast39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row477_col6" class="data row477 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row478" class="row_heading level0 row478" >478</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col0" class="data row478 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col1" class="data row478 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col2" class="data row478 col2" >168</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col3" class="data row478 col3" >Sun Strike, Jaws of Twisted Visions</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col4" class="data row478 col4" >$2.64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col5" class="data row478 col5" >Yaralnura48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row478_col6" class="data row478 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row479" class="row_heading level0 row479" >479</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col0" class="data row479 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col1" class="data row479 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col2" class="data row479 col2" >48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col3" class="data row479 col3" >Rage, Legacy of the Lone Victor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col4" class="data row479 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col5" class="data row479 col5" >Isursti83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row479_col6" class="data row479 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row480" class="row_heading level0 row480" >480</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col0" class="data row480 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col1" class="data row480 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col2" class="data row480 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col3" class="data row480 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col4" class="data row480 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col5" class="data row480 col5" >Phairinum94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row480_col6" class="data row480 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row481" class="row_heading level0 row481" >481</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col0" class="data row481 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col1" class="data row481 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col2" class="data row481 col2" >151</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col3" class="data row481 col3" >Severance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col4" class="data row481 col4" >$1.85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col5" class="data row481 col5" >Ethralan59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row481_col6" class="data row481 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row482" class="row_heading level0 row482" >482</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col0" class="data row482 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col1" class="data row482 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col2" class="data row482 col2" >165</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col3" class="data row482 col3" >Bone Crushing Silver Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col4" class="data row482 col4" >$3.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col5" class="data row482 col5" >Raelly43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row482_col6" class="data row482 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row483" class="row_heading level0 row483" >483</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col0" class="data row483 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col1" class="data row483 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col2" class="data row483 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col3" class="data row483 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col4" class="data row483 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col5" class="data row483 col5" >Lisassasta50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row483_col6" class="data row483 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row484" class="row_heading level0 row484" >484</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col0" class="data row484 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col1" class="data row484 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col2" class="data row484 col2" >104</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col3" class="data row484 col3" >Gladiator's Glaive</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col4" class="data row484 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col5" class="data row484 col5" >Chanastnya43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row484_col6" class="data row484 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row485" class="row_heading level0 row485" >485</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col0" class="data row485 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col1" class="data row485 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col2" class="data row485 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col3" class="data row485 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col4" class="data row485 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col5" class="data row485 col5" >Sondimla25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row485_col6" class="data row485 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row486" class="row_heading level0 row486" >486</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col0" class="data row486 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col1" class="data row486 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col2" class="data row486 col2" >136</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col3" class="data row486 col3" >Ghastly Adamantite Protector</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col4" class="data row486 col4" >$3.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col5" class="data row486 col5" >Chamilsala65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row486_col6" class="data row486 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row487" class="row_heading level0 row487" >487</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col0" class="data row487 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col1" class="data row487 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col2" class="data row487 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col3" class="data row487 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col4" class="data row487 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col5" class="data row487 col5" >Idaria87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row487_col6" class="data row487 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row488" class="row_heading level0 row488" >488</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col0" class="data row488 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col1" class="data row488 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col2" class="data row488 col2" >76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col3" class="data row488 col3" >Haunted Bronzed Bludgeon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col4" class="data row488 col4" >$4.12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col5" class="data row488 col5" >Eoda93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row488_col6" class="data row488 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row489" class="row_heading level0 row489" >489</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col0" class="data row489 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col1" class="data row489 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col2" class="data row489 col2" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col3" class="data row489 col3" >Souleater</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col4" class="data row489 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col5" class="data row489 col5" >Chanastst38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row489_col6" class="data row489 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row490" class="row_heading level0 row490" >490</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col0" class="data row490 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col1" class="data row490 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col2" class="data row490 col2" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col3" class="data row490 col3" >Second Chance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col4" class="data row490 col4" >$2.34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col5" class="data row490 col5" >Lamil79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row490_col6" class="data row490 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row491" class="row_heading level0 row491" >491</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col0" class="data row491 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col1" class="data row491 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col2" class="data row491 col2" >161</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col3" class="data row491 col3" >Devine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col4" class="data row491 col4" >$1.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col5" class="data row491 col5" >Liri91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row491_col6" class="data row491 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row492" class="row_heading level0 row492" >492</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col0" class="data row492 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col1" class="data row492 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col2" class="data row492 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col3" class="data row492 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col4" class="data row492 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col5" class="data row492 col5" >Qaronon57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row492_col6" class="data row492 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row493" class="row_heading level0 row493" >493</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col0" class="data row493 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col1" class="data row493 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col2" class="data row493 col2" >57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col3" class="data row493 col3" >Despair, Favor of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col4" class="data row493 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col5" class="data row493 col5" >Chadjask77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row493_col6" class="data row493 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row494" class="row_heading level0 row494" >494</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col0" class="data row494 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col1" class="data row494 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col2" class="data row494 col2" >52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col3" class="data row494 col3" >Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col4" class="data row494 col4" >$4.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col5" class="data row494 col5" >Ethralista69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row494_col6" class="data row494 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row495" class="row_heading level0 row495" >495</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col0" class="data row495 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col1" class="data row495 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col2" class="data row495 col2" >49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col3" class="data row495 col3" >The Oculus, Token of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col4" class="data row495 col4" >$4.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col5" class="data row495 col5" >Phaeduesurgue38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row495_col6" class="data row495 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row496" class="row_heading level0 row496" >496</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col0" class="data row496 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col1" class="data row496 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col2" class="data row496 col2" >95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col3" class="data row496 col3" >Singed Onyx Warscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col4" class="data row496 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col5" class="data row496 col5" >Rathellorin54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row496_col6" class="data row496 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row497" class="row_heading level0 row497" >497</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col0" class="data row497 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col1" class="data row497 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col2" class="data row497 col2" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col3" class="data row497 col3" >Second Chance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col4" class="data row497 col4" >$2.34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col5" class="data row497 col5" >Filon68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row497_col6" class="data row497 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row498" class="row_heading level0 row498" >498</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col0" class="data row498 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col1" class="data row498 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col2" class="data row498 col2" >160</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col3" class="data row498 col3" >Azurewrath</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col4" class="data row498 col4" >$2.22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col5" class="data row498 col5" >Chamilsala65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row498_col6" class="data row498 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row499" class="row_heading level0 row499" >499</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col0" class="data row499 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col1" class="data row499 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col2" class="data row499 col2" >1</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col3" class="data row499 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col4" class="data row499 col4" >$2.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col5" class="data row499 col5" >Assylla81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row499_col6" class="data row499 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row500" class="row_heading level0 row500" >500</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col0" class="data row500 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col1" class="data row500 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col2" class="data row500 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col3" class="data row500 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col4" class="data row500 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col5" class="data row500 col5" >Ingonon91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row500_col6" class="data row500 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row501" class="row_heading level0 row501" >501</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col0" class="data row501 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col1" class="data row501 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col2" class="data row501 col2" >144</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col3" class="data row501 col3" >Blood Infused Guardian</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col4" class="data row501 col4" >$2.86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col5" class="data row501 col5" >Lisovynya38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row501_col6" class="data row501 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row502" class="row_heading level0 row502" >502</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col0" class="data row502 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col1" class="data row502 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col2" class="data row502 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col3" class="data row502 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col4" class="data row502 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col5" class="data row502 col5" >Assesi91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row502_col6" class="data row502 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row503" class="row_heading level0 row503" >503</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col0" class="data row503 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col1" class="data row503 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col2" class="data row503 col2" >125</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col3" class="data row503 col3" >Whistling Mithril Warblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col4" class="data row503 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col5" class="data row503 col5" >Aellyria80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row503_col6" class="data row503 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row504" class="row_heading level0 row504" >504</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col0" class="data row504 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col1" class="data row504 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col2" class="data row504 col2" >176</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col3" class="data row504 col3" >Relentless Iron Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col4" class="data row504 col4" >$2.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col5" class="data row504 col5" >Aethedru70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row504_col6" class="data row504 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row505" class="row_heading level0 row505" >505</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col0" class="data row505 col0" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col1" class="data row505 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col2" class="data row505 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col3" class="data row505 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col4" class="data row505 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col5" class="data row505 col5" >Iladarla40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row505_col6" class="data row505 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row506" class="row_heading level0 row506" >506</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col0" class="data row506 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col1" class="data row506 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col2" class="data row506 col2" >180</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col3" class="data row506 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col4" class="data row506 col4" >$2.78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col5" class="data row506 col5" >Tyalaesu89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row506_col6" class="data row506 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row507" class="row_heading level0 row507" >507</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col0" class="data row507 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col1" class="data row507 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col2" class="data row507 col2" >161</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col3" class="data row507 col3" >Devine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col4" class="data row507 col4" >$1.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col5" class="data row507 col5" >Erudrion71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row507_col6" class="data row507 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row508" class="row_heading level0 row508" >508</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col0" class="data row508 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col1" class="data row508 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col2" class="data row508 col2" >181</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col3" class="data row508 col3" >Reaper's Toll</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col4" class="data row508 col4" >$4.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col5" class="data row508 col5" >Tyisriphos58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row508_col6" class="data row508 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row509" class="row_heading level0 row509" >509</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col0" class="data row509 col0" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col1" class="data row509 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col2" class="data row509 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col3" class="data row509 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col4" class="data row509 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col5" class="data row509 col5" >Iskista88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row509_col6" class="data row509 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row510" class="row_heading level0 row510" >510</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col0" class="data row510 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col1" class="data row510 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col2" class="data row510 col2" >133</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col3" class="data row510 col3" >Faith's Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col4" class="data row510 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col5" class="data row510 col5" >Seudaillorap38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row510_col6" class="data row510 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row511" class="row_heading level0 row511" >511</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col0" class="data row511 col0" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col1" class="data row511 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col2" class="data row511 col2" >70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col3" class="data row511 col3" >Hope's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col4" class="data row511 col4" >$3.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col5" class="data row511 col5" >Sondossa55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row511_col6" class="data row511 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row512" class="row_heading level0 row512" >512</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col0" class="data row512 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col1" class="data row512 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col2" class="data row512 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col3" class="data row512 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col4" class="data row512 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col5" class="data row512 col5" >Tyirithnu40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row512_col6" class="data row512 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row513" class="row_heading level0 row513" >513</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col0" class="data row513 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col1" class="data row513 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col2" class="data row513 col2" >159</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col3" class="data row513 col3" >Oathbreaker, Spellblade of Trials</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col4" class="data row513 col4" >$3.01</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col5" class="data row513 col5" >Malista67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row513_col6" class="data row513 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row514" class="row_heading level0 row514" >514</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col0" class="data row514 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col1" class="data row514 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col2" class="data row514 col2" >120</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col3" class="data row514 col3" >Agatha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col4" class="data row514 col4" >$1.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col5" class="data row514 col5" >Ristydru66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row514_col6" class="data row514 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row515" class="row_heading level0 row515" >515</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col0" class="data row515 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col1" class="data row515 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col2" class="data row515 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col3" class="data row515 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col4" class="data row515 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col5" class="data row515 col5" >Yasriphos60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row515_col6" class="data row515 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row516" class="row_heading level0 row516" >516</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col0" class="data row516 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col1" class="data row516 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col2" class="data row516 col2" >111</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col3" class="data row516 col3" >Misery's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col4" class="data row516 col4" >$2.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col5" class="data row516 col5" >Phainasu47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row516_col6" class="data row516 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row517" class="row_heading level0 row517" >517</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col0" class="data row517 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col1" class="data row517 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col2" class="data row517 col2" >81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col3" class="data row517 col3" >Dreamkiss</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col4" class="data row517 col4" >$4.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col5" class="data row517 col5" >Eural50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row517_col6" class="data row517 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row518" class="row_heading level0 row518" >518</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col0" class="data row518 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col1" class="data row518 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col2" class="data row518 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col3" class="data row518 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col4" class="data row518 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col5" class="data row518 col5" >Mindassast27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row518_col6" class="data row518 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row519" class="row_heading level0 row519" >519</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col0" class="data row519 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col1" class="data row519 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col2" class="data row519 col2" >62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col3" class="data row519 col3" >Piece Maker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col4" class="data row519 col4" >$4.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col5" class="data row519 col5" >Iskossan49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row519_col6" class="data row519 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row520" class="row_heading level0 row520" >520</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col0" class="data row520 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col1" class="data row520 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col2" class="data row520 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col3" class="data row520 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col4" class="data row520 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col5" class="data row520 col5" >Qarrian82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row520_col6" class="data row520 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row521" class="row_heading level0 row521" >521</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col0" class="data row521 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col1" class="data row521 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col2" class="data row521 col2" >170</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col3" class="data row521 col3" >Shadowsteel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col4" class="data row521 col4" >$1.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col5" class="data row521 col5" >Eulidru49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row521_col6" class="data row521 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row522" class="row_heading level0 row522" >522</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col0" class="data row522 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col1" class="data row522 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col2" class="data row522 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col3" class="data row522 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col4" class="data row522 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col5" class="data row522 col5" >Inguard95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row522_col6" class="data row522 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row523" class="row_heading level0 row523" >523</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col0" class="data row523 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col1" class="data row523 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col2" class="data row523 col2" >161</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col3" class="data row523 col3" >Devine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col4" class="data row523 col4" >$1.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col5" class="data row523 col5" >Hiral75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row523_col6" class="data row523 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row524" class="row_heading level0 row524" >524</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col0" class="data row524 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col1" class="data row524 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col2" class="data row524 col2" >162</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col3" class="data row524 col3" >Abyssal Shard</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col4" class="data row524 col4" >$2.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col5" class="data row524 col5" >Undast38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row524_col6" class="data row524 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row525" class="row_heading level0 row525" >525</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col0" class="data row525 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col1" class="data row525 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col2" class="data row525 col2" >182</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col3" class="data row525 col3" >Toothpick</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col4" class="data row525 col4" >$3.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col5" class="data row525 col5" >Chadjask77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row525_col6" class="data row525 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row526" class="row_heading level0 row526" >526</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col0" class="data row526 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col1" class="data row526 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col2" class="data row526 col2" >143</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col3" class="data row526 col3" >Frenzied Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col4" class="data row526 col4" >$2.60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col5" class="data row526 col5" >Marim28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row526_col6" class="data row526 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row527" class="row_heading level0 row527" >527</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col0" class="data row527 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col1" class="data row527 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col2" class="data row527 col2" >55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col3" class="data row527 col3" >Vindictive Glass Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col4" class="data row527 col4" >$4.26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col5" class="data row527 col5" >Yasriphos60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row527_col6" class="data row527 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row528" class="row_heading level0 row528" >528</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col0" class="data row528 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col1" class="data row528 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col2" class="data row528 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col3" class="data row528 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col4" class="data row528 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col5" class="data row528 col5" >Ialistidru50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row528_col6" class="data row528 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row529" class="row_heading level0 row529" >529</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col0" class="data row529 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col1" class="data row529 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col2" class="data row529 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col3" class="data row529 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col4" class="data row529 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col5" class="data row529 col5" >Aelalis34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row529_col6" class="data row529 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row530" class="row_heading level0 row530" >530</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col0" class="data row530 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col1" class="data row530 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col2" class="data row530 col2" >113</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col3" class="data row530 col3" >Solitude's Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col4" class="data row530 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col5" class="data row530 col5" >Airal46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row530_col6" class="data row530 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row531" class="row_heading level0 row531" >531</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col0" class="data row531 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col1" class="data row531 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col2" class="data row531 col2" >80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col3" class="data row531 col3" >Dreamsong</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col4" class="data row531 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col5" class="data row531 col5" >Lirtosia72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row531_col6" class="data row531 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row532" class="row_heading level0 row532" >532</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col0" class="data row532 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col1" class="data row532 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col2" class="data row532 col2" >177</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col3" class="data row532 col3" >Winterthorn, Defender of Shifting Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col4" class="data row532 col4" >$4.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col5" class="data row532 col5" >Assassasta79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row532_col6" class="data row532 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row533" class="row_heading level0 row533" >533</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col0" class="data row533 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col1" class="data row533 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col2" class="data row533 col2" >183</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col3" class="data row533 col3" >Dragon's Greatsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col4" class="data row533 col4" >$2.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col5" class="data row533 col5" >Saerallora71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row533_col6" class="data row533 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row534" class="row_heading level0 row534" >534</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col0" class="data row534 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col1" class="data row534 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col2" class="data row534 col2" >98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col3" class="data row534 col3" >Deadline, Voice Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col4" class="data row534 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col5" class="data row534 col5" >Frichossast86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row534_col6" class="data row534 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row535" class="row_heading level0 row535" >535</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col0" class="data row535 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col1" class="data row535 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col2" class="data row535 col2" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col3" class="data row535 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col4" class="data row535 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col5" class="data row535 col5" >Undirra73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row535_col6" class="data row535 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row536" class="row_heading level0 row536" >536</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col0" class="data row536 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col1" class="data row536 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col2" class="data row536 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col3" class="data row536 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col4" class="data row536 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col5" class="data row536 col5" >Chanastsda67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row536_col6" class="data row536 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row537" class="row_heading level0 row537" >537</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col0" class="data row537 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col1" class="data row537 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col2" class="data row537 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col3" class="data row537 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col4" class="data row537 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col5" class="data row537 col5" >Undirrala66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row537_col6" class="data row537 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row538" class="row_heading level0 row538" >538</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col0" class="data row538 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col1" class="data row538 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col2" class="data row538 col2" >183</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col3" class="data row538 col3" >Dragon's Greatsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col4" class="data row538 col4" >$2.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col5" class="data row538 col5" >Lirtosia72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row538_col6" class="data row538 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row539" class="row_heading level0 row539" >539</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col0" class="data row539 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col1" class="data row539 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col2" class="data row539 col2" >171</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col3" class="data row539 col3" >Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col4" class="data row539 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col5" class="data row539 col5" >Phaestycal84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row539_col6" class="data row539 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row540" class="row_heading level0 row540" >540</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col0" class="data row540 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col1" class="data row540 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col2" class="data row540 col2" >153</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col3" class="data row540 col3" >Mercenary Sabre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col4" class="data row540 col4" >$4.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col5" class="data row540 col5" >Malunil62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row540_col6" class="data row540 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row541" class="row_heading level0 row541" >541</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col0" class="data row541 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col1" class="data row541 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col2" class="data row541 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col3" class="data row541 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col4" class="data row541 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col5" class="data row541 col5" >Eosursurap97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row541_col6" class="data row541 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row542" class="row_heading level0 row542" >542</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col0" class="data row542 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col1" class="data row542 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col2" class="data row542 col2" >153</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col3" class="data row542 col3" >Mercenary Sabre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col4" class="data row542 col4" >$4.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col5" class="data row542 col5" >Iaralrgue74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row542_col6" class="data row542 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row543" class="row_heading level0 row543" >543</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col0" class="data row543 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col1" class="data row543 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col2" class="data row543 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col3" class="data row543 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col4" class="data row543 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col5" class="data row543 col5" >Seolollo93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row543_col6" class="data row543 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row544" class="row_heading level0 row544" >544</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col0" class="data row544 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col1" class="data row544 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col2" class="data row544 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col3" class="data row544 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col4" class="data row544 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col5" class="data row544 col5" >Ililsan66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row544_col6" class="data row544 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row545" class="row_heading level0 row545" >545</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col0" class="data row545 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col1" class="data row545 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col2" class="data row545 col2" >171</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col3" class="data row545 col3" >Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col4" class="data row545 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col5" class="data row545 col5" >Yasriphos60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row545_col6" class="data row545 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row546" class="row_heading level0 row546" >546</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col0" class="data row546 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col1" class="data row546 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col2" class="data row546 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col3" class="data row546 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col4" class="data row546 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col5" class="data row546 col5" >Iskosia51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row546_col6" class="data row546 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row547" class="row_heading level0 row547" >547</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col0" class="data row547 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col1" class="data row547 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col2" class="data row547 col2" >171</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col3" class="data row547 col3" >Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col4" class="data row547 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col5" class="data row547 col5" >Isurria36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row547_col6" class="data row547 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row548" class="row_heading level0 row548" >548</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col0" class="data row548 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col1" class="data row548 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col2" class="data row548 col2" >129</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col3" class="data row548 col3" >Fate, Vengeance of Eternal Justice</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col4" class="data row548 col4" >$1.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col5" class="data row548 col5" >Asur53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row548_col6" class="data row548 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row549" class="row_heading level0 row549" >549</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col0" class="data row549 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col1" class="data row549 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col2" class="data row549 col2" >135</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col3" class="data row549 col3" >Warped Diamond Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col4" class="data row549 col4" >$4.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col5" class="data row549 col5" >Aesur96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row549_col6" class="data row549 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row550" class="row_heading level0 row550" >550</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col0" class="data row550 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col1" class="data row550 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col2" class="data row550 col2" >108</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col3" class="data row550 col3" >Extraction, Quickblade Of Trembling Hands</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col4" class="data row550 col4" >$3.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col5" class="data row550 col5" >Iskosian40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row550_col6" class="data row550 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row551" class="row_heading level0 row551" >551</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col0" class="data row551 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col1" class="data row551 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col2" class="data row551 col2" >100</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col3" class="data row551 col3" >Blindscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col4" class="data row551 col4" >$3.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col5" class="data row551 col5" >Ililsa62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row551_col6" class="data row551 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row552" class="row_heading level0 row552" >552</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col0" class="data row552 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col1" class="data row552 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col2" class="data row552 col2" >60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col3" class="data row552 col3" >Wolf</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col4" class="data row552 col4" >$1.84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col5" class="data row552 col5" >Aillyriadru65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row552_col6" class="data row552 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row553" class="row_heading level0 row553" >553</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col0" class="data row553 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col1" class="data row553 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col2" class="data row553 col2" >110</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col3" class="data row553 col3" >Suspension</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col4" class="data row553 col4" >$2.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col5" class="data row553 col5" >Lisassa49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row553_col6" class="data row553 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row554" class="row_heading level0 row554" >554</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col0" class="data row554 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col1" class="data row554 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col2" class="data row554 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col3" class="data row554 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col4" class="data row554 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col5" class="data row554 col5" >Lisistaya47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row554_col6" class="data row554 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row555" class="row_heading level0 row555" >555</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col0" class="data row555 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col1" class="data row555 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col2" class="data row555 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col3" class="data row555 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col4" class="data row555 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col5" class="data row555 col5" >Ialidru40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row555_col6" class="data row555 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row556" class="row_heading level0 row556" >556</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col0" class="data row556 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col1" class="data row556 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col2" class="data row556 col2" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col3" class="data row556 col3" >Heartless Bone Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col4" class="data row556 col4" >$2.63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col5" class="data row556 col5" >Sondim43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row556_col6" class="data row556 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row557" class="row_heading level0 row557" >557</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col0" class="data row557 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col1" class="data row557 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col2" class="data row557 col2" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col3" class="data row557 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col4" class="data row557 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col5" class="data row557 col5" >Iskimnya76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row557_col6" class="data row557 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row558" class="row_heading level0 row558" >558</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col0" class="data row558 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col1" class="data row558 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col2" class="data row558 col2" >119</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col3" class="data row558 col3" >Stormbringer, Dark Blade of Ending Misery</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col4" class="data row558 col4" >$2.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col5" class="data row558 col5" >Aethe80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row558_col6" class="data row558 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row559" class="row_heading level0 row559" >559</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col0" class="data row559 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col1" class="data row559 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col2" class="data row559 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col3" class="data row559 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col4" class="data row559 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col5" class="data row559 col5" >Rathellorin54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row559_col6" class="data row559 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row560" class="row_heading level0 row560" >560</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col0" class="data row560 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col1" class="data row560 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col2" class="data row560 col2" >64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col3" class="data row560 col3" >Fusion Pummel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col4" class="data row560 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col5" class="data row560 col5" >Chanadar44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row560_col6" class="data row560 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row561" class="row_heading level0 row561" >561</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col0" class="data row561 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col1" class="data row561 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col2" class="data row561 col2" >83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col3" class="data row561 col3" >Lifebender</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col4" class="data row561 col4" >$3.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col5" class="data row561 col5" >Eudasu82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row561_col6" class="data row561 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row562" class="row_heading level0 row562" >562</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col0" class="data row562 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col1" class="data row562 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col2" class="data row562 col2" >88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col3" class="data row562 col3" >Emberling, Defender of Delusions</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col4" class="data row562 col4" >$4.10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col5" class="data row562 col5" >Lisirraya76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row562_col6" class="data row562 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row563" class="row_heading level0 row563" >563</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col0" class="data row563 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col1" class="data row563 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col2" class="data row563 col2" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col3" class="data row563 col3" >Unholy Wand</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col4" class="data row563 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col5" class="data row563 col5" >Lisossa25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row563_col6" class="data row563 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row564" class="row_heading level0 row564" >564</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col0" class="data row564 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col1" class="data row564 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col2" class="data row564 col2" >133</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col3" class="data row564 col3" >Faith's Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col4" class="data row564 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col5" class="data row564 col5" >Haedasu65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row564_col6" class="data row564 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row565" class="row_heading level0 row565" >565</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col0" class="data row565 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col1" class="data row565 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col2" class="data row565 col2" >97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col3" class="data row565 col3" >Swan Song, Gouger Of Terror</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col4" class="data row565 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col5" class="data row565 col5" >Iral74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row565_col6" class="data row565 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row566" class="row_heading level0 row566" >566</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col0" class="data row566 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col1" class="data row566 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col2" class="data row566 col2" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col3" class="data row566 col3" >Restored Bauble</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col4" class="data row566 col4" >$3.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col5" class="data row566 col5" >Lisjaskya84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row566_col6" class="data row566 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row567" class="row_heading level0 row567" >567</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col0" class="data row567 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col1" class="data row567 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col2" class="data row567 col2" >181</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col3" class="data row567 col3" >Reaper's Toll</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col4" class="data row567 col4" >$4.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col5" class="data row567 col5" >Saelaephos52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row567_col6" class="data row567 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row568" class="row_heading level0 row568" >568</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col0" class="data row568 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col1" class="data row568 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col2" class="data row568 col2" >76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col3" class="data row568 col3" >Haunted Bronzed Bludgeon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col4" class="data row568 col4" >$4.12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col5" class="data row568 col5" >Chamim85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row568_col6" class="data row568 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row569" class="row_heading level0 row569" >569</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col0" class="data row569 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col1" class="data row569 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col2" class="data row569 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col3" class="data row569 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col4" class="data row569 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col5" class="data row569 col5" >Chamadar61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row569_col6" class="data row569 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row570" class="row_heading level0 row570" >570</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col0" class="data row570 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col1" class="data row570 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col2" class="data row570 col2" >142</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col3" class="data row570 col3" >Righteous Might</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col4" class="data row570 col4" >$4.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col5" class="data row570 col5" >Lirtista72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row570_col6" class="data row570 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row571" class="row_heading level0 row571" >571</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col0" class="data row571 col0" >17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col1" class="data row571 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col2" class="data row571 col2" >113</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col3" class="data row571 col3" >Solitude's Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col4" class="data row571 col4" >$2.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col5" class="data row571 col5" >Seudanu38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row571_col6" class="data row571 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row572" class="row_heading level0 row572" >572</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col0" class="data row572 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col1" class="data row572 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col2" class="data row572 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col3" class="data row572 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col4" class="data row572 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col5" class="data row572 col5" >Lisossa63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row572_col6" class="data row572 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row573" class="row_heading level0 row573" >573</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col0" class="data row573 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col1" class="data row573 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col2" class="data row573 col2" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col3" class="data row573 col3" >Spectral Bone Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col4" class="data row573 col4" >$2.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col5" class="data row573 col5" >Siathecal92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row573_col6" class="data row573 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row574" class="row_heading level0 row574" >574</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col0" class="data row574 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col1" class="data row574 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col2" class="data row574 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col3" class="data row574 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col4" class="data row574 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col5" class="data row574 col5" >Eullydru35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row574_col6" class="data row574 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row575" class="row_heading level0 row575" >575</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col0" class="data row575 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col1" class="data row575 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col2" class="data row575 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col3" class="data row575 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col4" class="data row575 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col5" class="data row575 col5" >Chamistast30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row575_col6" class="data row575 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row576" class="row_heading level0 row576" >576</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col0" class="data row576 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col1" class="data row576 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col2" class="data row576 col2" >142</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col3" class="data row576 col3" >Righteous Might</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col4" class="data row576 col4" >$4.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col5" class="data row576 col5" >Isrirgue68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row576_col6" class="data row576 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row577" class="row_heading level0 row577" >577</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col0" class="data row577 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col1" class="data row577 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col2" class="data row577 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col3" class="data row577 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col4" class="data row577 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col5" class="data row577 col5" >Eurallo89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row577_col6" class="data row577 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row578" class="row_heading level0 row578" >578</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col0" class="data row578 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col1" class="data row578 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col2" class="data row578 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col3" class="data row578 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col4" class="data row578 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col5" class="data row578 col5" >Raithe71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row578_col6" class="data row578 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row579" class="row_heading level0 row579" >579</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col0" class="data row579 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col1" class="data row579 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col2" class="data row579 col2" >151</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col3" class="data row579 col3" >Severance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col4" class="data row579 col4" >$1.85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col5" class="data row579 col5" >Iskossaya95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row579_col6" class="data row579 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row580" class="row_heading level0 row580" >580</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col0" class="data row580 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col1" class="data row580 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col2" class="data row580 col2" >178</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col3" class="data row580 col3" >Oathbreaker, Last Hope of the Breaking Storm</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col4" class="data row580 col4" >$2.41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col5" class="data row580 col5" >Yathecal82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row580_col6" class="data row580 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row581" class="row_heading level0 row581" >581</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col0" class="data row581 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col1" class="data row581 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col2" class="data row581 col2" >68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col3" class="data row581 col3" >Storm-Weaver, Slayer of Inception</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col4" class="data row581 col4" >$2.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col5" class="data row581 col5" >Filrion44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row581_col6" class="data row581 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row582" class="row_heading level0 row582" >582</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col0" class="data row582 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col1" class="data row582 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col2" class="data row582 col2" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col3" class="data row582 col3" >Unholy Wand</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col4" class="data row582 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col5" class="data row582 col5" >Saralp86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row582_col6" class="data row582 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row583" class="row_heading level0 row583" >583</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col0" class="data row583 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col1" class="data row583 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col2" class="data row583 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col3" class="data row583 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col4" class="data row583 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col5" class="data row583 col5" >Tyeuduen32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row583_col6" class="data row583 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row584" class="row_heading level0 row584" >584</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col0" class="data row584 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col1" class="data row584 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col2" class="data row584 col2" >174</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col3" class="data row584 col3" >Primitive Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col4" class="data row584 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col5" class="data row584 col5" >Aina43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row584_col6" class="data row584 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row585" class="row_heading level0 row585" >585</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col0" class="data row585 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col1" class="data row585 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col2" class="data row585 col2" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col3" class="data row585 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col4" class="data row585 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col5" class="data row585 col5" >Undiwinya88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row585_col6" class="data row585 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row586" class="row_heading level0 row586" >586</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col0" class="data row586 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col1" class="data row586 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col2" class="data row586 col2" >75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col3" class="data row586 col3" >Brutality Ivory Warmace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col4" class="data row586 col4" >$1.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col5" class="data row586 col5" >Silaera56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row586_col6" class="data row586 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row587" class="row_heading level0 row587" >587</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col0" class="data row587 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col1" class="data row587 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col2" class="data row587 col2" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col3" class="data row587 col3" >Riddle, Tribute of Ended Dreams</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col4" class="data row587 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col5" class="data row587 col5" >Iskadarya95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row587_col6" class="data row587 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row588" class="row_heading level0 row588" >588</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col0" class="data row588 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col1" class="data row588 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col2" class="data row588 col2" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col3" class="data row588 col3" >Unholy Wand</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col4" class="data row588 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col5" class="data row588 col5" >Eoralphos86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row588_col6" class="data row588 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row589" class="row_heading level0 row589" >589</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col0" class="data row589 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col1" class="data row589 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col2" class="data row589 col2" >144</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col3" class="data row589 col3" >Blood Infused Guardian</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col4" class="data row589 col4" >$2.86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col5" class="data row589 col5" >Billysu76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row589_col6" class="data row589 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row590" class="row_heading level0 row590" >590</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col0" class="data row590 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col1" class="data row590 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col2" class="data row590 col2" >152</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col3" class="data row590 col3" >Darkheart</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col4" class="data row590 col4" >$3.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col5" class="data row590 col5" >Seorithstilis90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row590_col6" class="data row590 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row591" class="row_heading level0 row591" >591</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col0" class="data row591 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col1" class="data row591 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col2" class="data row591 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col3" class="data row591 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col4" class="data row591 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col5" class="data row591 col5" >Aidaira48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row591_col6" class="data row591 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row592" class="row_heading level0 row592" >592</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col0" class="data row592 col0" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col1" class="data row592 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col2" class="data row592 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col3" class="data row592 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col4" class="data row592 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col5" class="data row592 col5" >Mindimnya67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row592_col6" class="data row592 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row593" class="row_heading level0 row593" >593</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col0" class="data row593 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col1" class="data row593 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col2" class="data row593 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col3" class="data row593 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col4" class="data row593 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col5" class="data row593 col5" >Euna48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row593_col6" class="data row593 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row594" class="row_heading level0 row594" >594</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col0" class="data row594 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col1" class="data row594 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col2" class="data row594 col2" >163</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col3" class="data row594 col3" >Thunderfury Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col4" class="data row594 col4" >$3.02</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col5" class="data row594 col5" >Lisassasta50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row594_col6" class="data row594 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row595" class="row_heading level0 row595" >595</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col0" class="data row595 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col1" class="data row595 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col2" class="data row595 col2" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col3" class="data row595 col3" >Stormcaller</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col4" class="data row595 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col5" class="data row595 col5" >Eusur90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row595_col6" class="data row595 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row596" class="row_heading level0 row596" >596</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col0" class="data row596 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col1" class="data row596 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col2" class="data row596 col2" >133</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col3" class="data row596 col3" >Faith's Scimitar</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col4" class="data row596 col4" >$3.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col5" class="data row596 col5" >Undirrala66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row596_col6" class="data row596 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row597" class="row_heading level0 row597" >597</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col0" class="data row597 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col1" class="data row597 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col2" class="data row597 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col3" class="data row597 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col4" class="data row597 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col5" class="data row597 col5" >Lamil70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row597_col6" class="data row597 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row598" class="row_heading level0 row598" >598</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col0" class="data row598 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col1" class="data row598 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col2" class="data row598 col2" >12</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col3" class="data row598 col3" >Dawne</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col4" class="data row598 col4" >$4.30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col5" class="data row598 col5" >Chamadarnya73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row598_col6" class="data row598 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row599" class="row_heading level0 row599" >599</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col0" class="data row599 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col1" class="data row599 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col2" class="data row599 col2" >6</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col3" class="data row599 col3" >Rusty Skull</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col4" class="data row599 col4" >$1.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col5" class="data row599 col5" >Ilast79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row599_col6" class="data row599 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row600" class="row_heading level0 row600" >600</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col0" class="data row600 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col1" class="data row600 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col2" class="data row600 col2" >97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col3" class="data row600 col3" >Swan Song, Gouger Of Terror</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col4" class="data row600 col4" >$3.58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col5" class="data row600 col5" >Sondilsa35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row600_col6" class="data row600 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row601" class="row_heading level0 row601" >601</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col0" class="data row601 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col1" class="data row601 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col2" class="data row601 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col3" class="data row601 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col4" class="data row601 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col5" class="data row601 col5" >Ralonurin90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row601_col6" class="data row601 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row602" class="row_heading level0 row602" >602</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col0" class="data row602 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col1" class="data row602 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col2" class="data row602 col2" >71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col3" class="data row602 col3" >Demise</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col4" class="data row602 col4" >$4.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col5" class="data row602 col5" >Marundi65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row602_col6" class="data row602 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row603" class="row_heading level0 row603" >603</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col0" class="data row603 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col1" class="data row603 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col2" class="data row603 col2" >60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col3" class="data row603 col3" >Wolf</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col4" class="data row603 col4" >$1.84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col5" class="data row603 col5" >Phaedan76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row603_col6" class="data row603 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row604" class="row_heading level0 row604" >604</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col0" class="data row604 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col1" class="data row604 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col2" class="data row604 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col3" class="data row604 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col4" class="data row604 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col5" class="data row604 col5" >Farenon57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row604_col6" class="data row604 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row605" class="row_heading level0 row605" >605</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col0" class="data row605 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col1" class="data row605 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col2" class="data row605 col2" >157</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col3" class="data row605 col3" >Spada, Etcher of Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col4" class="data row605 col4" >$2.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col5" class="data row605 col5" >Ilassa51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row605_col6" class="data row605 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row606" class="row_heading level0 row606" >606</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col0" class="data row606 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col1" class="data row606 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col2" class="data row606 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col3" class="data row606 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col4" class="data row606 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col5" class="data row606 col5" >Lirtossa84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row606_col6" class="data row606 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row607" class="row_heading level0 row607" >607</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col0" class="data row607 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col1" class="data row607 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col2" class="data row607 col2" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col3" class="data row607 col3" >The Void, Vengeance of Dark Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col4" class="data row607 col4" >$2.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col5" class="data row607 col5" >Airi27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row607_col6" class="data row607 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row608" class="row_heading level0 row608" >608</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col0" class="data row608 col0" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col1" class="data row608 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col2" class="data row608 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col3" class="data row608 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col4" class="data row608 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col5" class="data row608 col5" >Indcil77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row608_col6" class="data row608 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row609" class="row_heading level0 row609" >609</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col0" class="data row609 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col1" class="data row609 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col2" class="data row609 col2" >53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col3" class="data row609 col3" >Vengeance Cleaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col4" class="data row609 col4" >$3.70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col5" class="data row609 col5" >Chamastya76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row609_col6" class="data row609 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row610" class="row_heading level0 row610" >610</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col0" class="data row610 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col1" class="data row610 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col2" class="data row610 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col3" class="data row610 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col4" class="data row610 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col5" class="data row610 col5" >Lassjask63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row610_col6" class="data row610 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row611" class="row_heading level0 row611" >611</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col0" class="data row611 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col1" class="data row611 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col2" class="data row611 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col3" class="data row611 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col4" class="data row611 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col5" class="data row611 col5" >Heolo60</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row611_col6" class="data row611 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row612" class="row_heading level0 row612" >612</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col0" class="data row612 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col1" class="data row612 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col2" class="data row612 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col3" class="data row612 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col4" class="data row612 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col5" class="data row612 col5" >Isurria36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row612_col6" class="data row612 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row613" class="row_heading level0 row613" >613</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col0" class="data row613 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col1" class="data row613 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col2" class="data row613 col2" >153</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col3" class="data row613 col3" >Mercenary Sabre</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col4" class="data row613 col4" >$4.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col5" class="data row613 col5" >Lisossan98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row613_col6" class="data row613 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row614" class="row_heading level0 row614" >614</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col0" class="data row614 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col1" class="data row614 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col2" class="data row614 col2" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col3" class="data row614 col3" >Pursuit, Cudgel of Necromancy</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col4" class="data row614 col4" >$3.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col5" class="data row614 col5" >Sondim43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row614_col6" class="data row614 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row615" class="row_heading level0 row615" >615</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col0" class="data row615 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col1" class="data row615 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col2" class="data row615 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col3" class="data row615 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col4" class="data row615 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col5" class="data row615 col5" >Mindirra92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row615_col6" class="data row615 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row616" class="row_heading level0 row616" >616</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col0" class="data row616 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col1" class="data row616 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col2" class="data row616 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col3" class="data row616 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col4" class="data row616 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col5" class="data row616 col5" >Reuthelis39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row616_col6" class="data row616 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row617" class="row_heading level0 row617" >617</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col0" class="data row617 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col1" class="data row617 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col2" class="data row617 col2" >166</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col3" class="data row617 col3" >Thirsty Iron Reaver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col4" class="data row617 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col5" class="data row617 col5" >Thourdirra92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row617_col6" class="data row617 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row618" class="row_heading level0 row618" >618</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col0" class="data row618 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col1" class="data row618 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col2" class="data row618 col2" >49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col3" class="data row618 col3" >The Oculus, Token of Lost Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col4" class="data row618 col4" >$4.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col5" class="data row618 col5" >Frichadar89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row618_col6" class="data row618 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row619" class="row_heading level0 row619" >619</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col0" class="data row619 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col1" class="data row619 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col2" class="data row619 col2" >123</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col3" class="data row619 col3" >Twilight's Carver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col4" class="data row619 col4" >$1.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col5" class="data row619 col5" >Raesursurap33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row619_col6" class="data row619 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row620" class="row_heading level0 row620" >620</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col0" class="data row620 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col1" class="data row620 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col2" class="data row620 col2" >80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col3" class="data row620 col3" >Dreamsong</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col4" class="data row620 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col5" class="data row620 col5" >Jiskilsa35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row620_col6" class="data row620 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row621" class="row_heading level0 row621" >621</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col0" class="data row621 col0" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col1" class="data row621 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col2" class="data row621 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col3" class="data row621 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col4" class="data row621 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col5" class="data row621 col5" >Philistirap41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row621_col6" class="data row621 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row622" class="row_heading level0 row622" >622</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col0" class="data row622 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col1" class="data row622 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col2" class="data row622 col2" >144</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col3" class="data row622 col3" >Blood Infused Guardian</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col4" class="data row622 col4" >$2.86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col5" class="data row622 col5" >Tyidainu31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row622_col6" class="data row622 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row623" class="row_heading level0 row623" >623</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col0" class="data row623 col0" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col1" class="data row623 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col2" class="data row623 col2" >161</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col3" class="data row623 col3" >Devine</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col4" class="data row623 col4" >$1.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col5" class="data row623 col5" >Mindimnya67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row623_col6" class="data row623 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row624" class="row_heading level0 row624" >624</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col0" class="data row624 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col1" class="data row624 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col2" class="data row624 col2" >95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col3" class="data row624 col3" >Singed Onyx Warscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col4" class="data row624 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col5" class="data row624 col5" >Tridaira71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row624_col6" class="data row624 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row625" class="row_heading level0 row625" >625</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col0" class="data row625 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col1" class="data row625 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col2" class="data row625 col2" >90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col3" class="data row625 col3" >Betrayer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col4" class="data row625 col4" >$1.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col5" class="data row625 col5" >Queusurra38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row625_col6" class="data row625 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row626" class="row_heading level0 row626" >626</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col0" class="data row626 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col1" class="data row626 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col2" class="data row626 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col3" class="data row626 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col4" class="data row626 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col5" class="data row626 col5" >Mindadaran26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row626_col6" class="data row626 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row627" class="row_heading level0 row627" >627</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col0" class="data row627 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col1" class="data row627 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col2" class="data row627 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col3" class="data row627 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col4" class="data row627 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col5" class="data row627 col5" >Lisassa39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row627_col6" class="data row627 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row628" class="row_heading level0 row628" >628</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col0" class="data row628 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col1" class="data row628 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col2" class="data row628 col2" >78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col3" class="data row628 col3" >Glimmer, Ender of the Moon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col4" class="data row628 col4" >$2.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col5" class="data row628 col5" >Alaesu77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row628_col6" class="data row628 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row629" class="row_heading level0 row629" >629</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col0" class="data row629 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col1" class="data row629 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col2" class="data row629 col2" >142</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col3" class="data row629 col3" >Righteous Might</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col4" class="data row629 col4" >$4.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col5" class="data row629 col5" >Ilogha82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row629_col6" class="data row629 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row630" class="row_heading level0 row630" >630</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col0" class="data row630 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col1" class="data row630 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col2" class="data row630 col2" >178</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col3" class="data row630 col3" >Oathbreaker, Last Hope of the Breaking Storm</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col4" class="data row630 col4" >$2.41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col5" class="data row630 col5" >Pharithdil38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row630_col6" class="data row630 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row631" class="row_heading level0 row631" >631</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col0" class="data row631 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col1" class="data row631 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col2" class="data row631 col2" >85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col3" class="data row631 col3" >Malificent Bag</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col4" class="data row631 col4" >$2.17</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col5" class="data row631 col5" >Mindossasya74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row631_col6" class="data row631 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row632" class="row_heading level0 row632" >632</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col0" class="data row632 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col1" class="data row632 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col2" class="data row632 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col3" class="data row632 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col4" class="data row632 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col5" class="data row632 col5" >Syadaillo88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row632_col6" class="data row632 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row633" class="row_heading level0 row633" >633</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col0" class="data row633 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col1" class="data row633 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col2" class="data row633 col2" >127</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col3" class="data row633 col3" >Heartseeker, Reaver of Souls</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col4" class="data row633 col4" >$3.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col5" class="data row633 col5" >Lassilsala30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row633_col6" class="data row633 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row634" class="row_heading level0 row634" >634</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col0" class="data row634 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col1" class="data row634 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col2" class="data row634 col2" >111</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col3" class="data row634 col3" >Misery's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col4" class="data row634 col4" >$2.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col5" class="data row634 col5" >Eusri26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row634_col6" class="data row634 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row635" class="row_heading level0 row635" >635</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col0" class="data row635 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col1" class="data row635 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col2" class="data row635 col2" >67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col3" class="data row635 col3" >Celeste, Incarnation of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col4" class="data row635 col4" >$2.31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col5" class="data row635 col5" >Chanastsda67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row635_col6" class="data row635 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row636" class="row_heading level0 row636" >636</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col0" class="data row636 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col1" class="data row636 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col2" class="data row636 col2" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col3" class="data row636 col3" >Second Chance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col4" class="data row636 col4" >$2.34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col5" class="data row636 col5" >Hilaerin92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row636_col6" class="data row636 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row637" class="row_heading level0 row637" >637</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col0" class="data row637 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col1" class="data row637 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col2" class="data row637 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col3" class="data row637 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col4" class="data row637 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col5" class="data row637 col5" >Aeliriam77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row637_col6" class="data row637 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row638" class="row_heading level0 row638" >638</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col0" class="data row638 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col1" class="data row638 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col2" class="data row638 col2" >83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col3" class="data row638 col3" >Lifebender</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col4" class="data row638 col4" >$3.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col5" class="data row638 col5" >Lirtossan50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row638_col6" class="data row638 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row639" class="row_heading level0 row639" >639</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col0" class="data row639 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col1" class="data row639 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col2" class="data row639 col2" >94</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col3" class="data row639 col3" >Mourning Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col4" class="data row639 col4" >$1.82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col5" class="data row639 col5" >Iskossan49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row639_col6" class="data row639 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row640" class="row_heading level0 row640" >640</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col0" class="data row640 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col1" class="data row640 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col2" class="data row640 col2" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col3" class="data row640 col3" >Amnesia</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col4" class="data row640 col4" >$3.57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col5" class="data row640 col5" >Sondim73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row640_col6" class="data row640 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row641" class="row_heading level0 row641" >641</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col0" class="data row641 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col1" class="data row641 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col2" class="data row641 col2" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col3" class="data row641 col3" >Shadow Strike, Glory of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col4" class="data row641 col4" >$1.93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col5" class="data row641 col5" >Assosia38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row641_col6" class="data row641 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row642" class="row_heading level0 row642" >642</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col0" class="data row642 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col1" class="data row642 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col2" class="data row642 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col3" class="data row642 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col4" class="data row642 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col5" class="data row642 col5" >Reula64</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row642_col6" class="data row642 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row643" class="row_heading level0 row643" >643</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col0" class="data row643 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col1" class="data row643 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col2" class="data row643 col2" >182</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col3" class="data row643 col3" >Toothpick</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col4" class="data row643 col4" >$3.48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col5" class="data row643 col5" >Tyeosri53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row643_col6" class="data row643 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row644" class="row_heading level0 row644" >644</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col0" class="data row644 col0" >43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col1" class="data row644 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col2" class="data row644 col2" >57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col3" class="data row644 col3" >Despair, Favor of Due Diligence</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col4" class="data row644 col4" >$3.81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col5" class="data row644 col5" >Raesurdil91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row644_col6" class="data row644 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row645" class="row_heading level0 row645" >645</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col0" class="data row645 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col1" class="data row645 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col2" class="data row645 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col3" class="data row645 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col4" class="data row645 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col5" class="data row645 col5" >Anallorgue57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row645_col6" class="data row645 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row646" class="row_heading level0 row646" >646</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col0" class="data row646 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col1" class="data row646 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col2" class="data row646 col2" >78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col3" class="data row646 col3" >Glimmer, Ender of the Moon</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col4" class="data row646 col4" >$2.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col5" class="data row646 col5" >Idai61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row646_col6" class="data row646 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row647" class="row_heading level0 row647" >647</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col0" class="data row647 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col1" class="data row647 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col2" class="data row647 col2" >156</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col3" class="data row647 col3" >Soul-Forged Steel Shortsword</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col4" class="data row647 col4" >$1.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col5" class="data row647 col5" >Aeduera68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row647_col6" class="data row647 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row648" class="row_heading level0 row648" >648</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col0" class="data row648 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col1" class="data row648 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col2" class="data row648 col2" >92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col3" class="data row648 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col4" class="data row648 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col5" class="data row648 col5" >Rithe53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row648_col6" class="data row648 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row649" class="row_heading level0 row649" >649</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col0" class="data row649 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col1" class="data row649 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col2" class="data row649 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col3" class="data row649 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col4" class="data row649 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col5" class="data row649 col5" >Quinarap53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row649_col6" class="data row649 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row650" class="row_heading level0 row650" >650</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col0" class="data row650 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col1" class="data row650 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col2" class="data row650 col2" >109</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col3" class="data row650 col3" >Downfall, Scalpel Of The Emperor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col4" class="data row650 col4" >$3.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col5" class="data row650 col5" >Haerithp41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row650_col6" class="data row650 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row651" class="row_heading level0 row651" >651</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col0" class="data row651 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col1" class="data row651 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col2" class="data row651 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col3" class="data row651 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col4" class="data row651 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col5" class="data row651 col5" >Seuthelis34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row651_col6" class="data row651 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row652" class="row_heading level0 row652" >652</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col0" class="data row652 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col1" class="data row652 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col2" class="data row652 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col3" class="data row652 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col4" class="data row652 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col5" class="data row652 col5" >Styaduen40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row652_col6" class="data row652 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row653" class="row_heading level0 row653" >653</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col0" class="data row653 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col1" class="data row653 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col2" class="data row653 col2" >120</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col3" class="data row653 col3" >Agatha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col4" class="data row653 col4" >$1.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col5" class="data row653 col5" >Ennoncil86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row653_col6" class="data row653 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row654" class="row_heading level0 row654" >654</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col0" class="data row654 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col1" class="data row654 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col2" class="data row654 col2" >120</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col3" class="data row654 col3" >Agatha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col4" class="data row654 col4" >$1.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col5" class="data row654 col5" >Lassassasda30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row654_col6" class="data row654 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row655" class="row_heading level0 row655" >655</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col0" class="data row655 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col1" class="data row655 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col2" class="data row655 col2" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col3" class="data row655 col3" >Sleepwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col4" class="data row655 col4" >$1.73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col5" class="data row655 col5" >Tyeosri53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row655_col6" class="data row655 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row656" class="row_heading level0 row656" >656</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col0" class="data row656 col0" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col1" class="data row656 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col2" class="data row656 col2" >63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col3" class="data row656 col3" >Stormfury Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col4" class="data row656 col4" >$1.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col5" class="data row656 col5" >Ilaststa70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row656_col6" class="data row656 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row657" class="row_heading level0 row657" >657</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col0" class="data row657 col0" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col1" class="data row657 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col2" class="data row657 col2" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col3" class="data row657 col3" >Orenmir</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col4" class="data row657 col4" >$4.95</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col5" class="data row657 col5" >Tyarithn67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row657_col6" class="data row657 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row658" class="row_heading level0 row658" >658</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col0" class="data row658 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col1" class="data row658 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col2" class="data row658 col2" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col3" class="data row658 col3" >Possessed Core</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col4" class="data row658 col4" >$1.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col5" class="data row658 col5" >Streural92</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row658_col6" class="data row658 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row659" class="row_heading level0 row659" >659</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col0" class="data row659 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col1" class="data row659 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col2" class="data row659 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col3" class="data row659 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col4" class="data row659 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col5" class="data row659 col5" >Haellysu29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row659_col6" class="data row659 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row660" class="row_heading level0 row660" >660</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col0" class="data row660 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col1" class="data row660 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col2" class="data row660 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col3" class="data row660 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col4" class="data row660 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col5" class="data row660 col5" >Yadaisuir65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row660_col6" class="data row660 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row661" class="row_heading level0 row661" >661</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col0" class="data row661 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col1" class="data row661 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col2" class="data row661 col2" >172</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col3" class="data row661 col3" >Blade of the Grave</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col4" class="data row661 col4" >$1.69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col5" class="data row661 col5" >Aerithnucal56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row661_col6" class="data row661 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row662" class="row_heading level0 row662" >662</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col0" class="data row662 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col1" class="data row662 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col2" class="data row662 col2" >77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col3" class="data row662 col3" >Piety, Guardian of Riddles</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col4" class="data row662 col4" >$3.68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col5" class="data row662 col5" >Sundjask71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row662_col6" class="data row662 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row663" class="row_heading level0 row663" >663</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col0" class="data row663 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col1" class="data row663 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col2" class="data row663 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col3" class="data row663 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col4" class="data row663 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col5" class="data row663 col5" >Tyisriphos58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row663_col6" class="data row663 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row664" class="row_heading level0 row664" >664</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col0" class="data row664 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col1" class="data row664 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col2" class="data row664 col2" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col3" class="data row664 col3" >Curved Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col4" class="data row664 col4" >$1.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col5" class="data row664 col5" >Sundaststa26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row664_col6" class="data row664 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row665" class="row_heading level0 row665" >665</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col0" class="data row665 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col1" class="data row665 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col2" class="data row665 col2" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col3" class="data row665 col3" >Warped Fetish</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col4" class="data row665 col4" >$2.41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col5" class="data row665 col5" >Yalo71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row665_col6" class="data row665 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row666" class="row_heading level0 row666" >666</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col0" class="data row666 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col1" class="data row666 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col2" class="data row666 col2" >67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col3" class="data row666 col3" >Celeste, Incarnation of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col4" class="data row666 col4" >$2.31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col5" class="data row666 col5" >Mindetosya30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row666_col6" class="data row666 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row667" class="row_heading level0 row667" >667</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col0" class="data row667 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col1" class="data row667 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col2" class="data row667 col2" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col3" class="data row667 col3" >Soul Infused Crystal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col4" class="data row667 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col5" class="data row667 col5" >Chanjaskan89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row667_col6" class="data row667 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row668" class="row_heading level0 row668" >668</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col0" class="data row668 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col1" class="data row668 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col2" class="data row668 col2" >124</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col3" class="data row668 col3" >Venom Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col4" class="data row668 col4" >$2.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col5" class="data row668 col5" >Chadjask77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row668_col6" class="data row668 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row669" class="row_heading level0 row669" >669</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col0" class="data row669 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col1" class="data row669 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col2" class="data row669 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col3" class="data row669 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col4" class="data row669 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col5" class="data row669 col5" >Lirtast83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row669_col6" class="data row669 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row670" class="row_heading level0 row670" >670</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col0" class="data row670 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col1" class="data row670 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col2" class="data row670 col2" >177</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col3" class="data row670 col3" >Winterthorn, Defender of Shifting Worlds</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col4" class="data row670 col4" >$4.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col5" class="data row670 col5" >Ingatcil75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row670_col6" class="data row670 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row671" class="row_heading level0 row671" >671</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col0" class="data row671 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col1" class="data row671 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col2" class="data row671 col2" >61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col3" class="data row671 col3" >Ragnarok</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col4" class="data row671 col4" >$3.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col5" class="data row671 col5" >Lassassast73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row671_col6" class="data row671 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row672" class="row_heading level0 row672" >672</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col0" class="data row672 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col1" class="data row672 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col2" class="data row672 col2" >157</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col3" class="data row672 col3" >Spada, Etcher of Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col4" class="data row672 col4" >$2.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col5" class="data row672 col5" >Strairisti57</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row672_col6" class="data row672 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row673" class="row_heading level0 row673" >673</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col0" class="data row673 col0" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col1" class="data row673 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col2" class="data row673 col2" >176</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col3" class="data row673 col3" >Relentless Iron Skewer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col4" class="data row673 col4" >$2.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col5" class="data row673 col5" >Qarwen67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row673_col6" class="data row673 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row674" class="row_heading level0 row674" >674</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col0" class="data row674 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col1" class="data row674 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col2" class="data row674 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col3" class="data row674 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col4" class="data row674 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col5" class="data row674 col5" >Filrion59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row674_col6" class="data row674 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row675" class="row_heading level0 row675" >675</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col0" class="data row675 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col1" class="data row675 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col2" class="data row675 col2" >118</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col3" class="data row675 col3" >Ghost Reaver, Longsword of Magic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col4" class="data row675 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col5" class="data row675 col5" >Sondim43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row675_col6" class="data row675 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row676" class="row_heading level0 row676" >676</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col0" class="data row676 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col1" class="data row676 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col2" class="data row676 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col3" class="data row676 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col4" class="data row676 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col5" class="data row676 col5" >Aellysup38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row676_col6" class="data row676 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row677" class="row_heading level0 row677" >677</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col0" class="data row677 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col1" class="data row677 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col2" class="data row677 col2" >75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col3" class="data row677 col3" >Brutality Ivory Warmace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col4" class="data row677 col4" >$1.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col5" class="data row677 col5" >Hala31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row677_col6" class="data row677 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row678" class="row_heading level0 row678" >678</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col0" class="data row678 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col1" class="data row678 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col2" class="data row678 col2" >65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col3" class="data row678 col3" >Conqueror Adamantite Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col4" class="data row678 col4" >$1.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col5" class="data row678 col5" >Rithe77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row678_col6" class="data row678 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row679" class="row_heading level0 row679" >679</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col0" class="data row679 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col1" class="data row679 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col2" class="data row679 col2" >159</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col3" class="data row679 col3" >Oathbreaker, Spellblade of Trials</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col4" class="data row679 col4" >$3.01</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col5" class="data row679 col5" >Marirrasta50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row679_col6" class="data row679 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row680" class="row_heading level0 row680" >680</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col0" class="data row680 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col1" class="data row680 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col2" class="data row680 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col3" class="data row680 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col4" class="data row680 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col5" class="data row680 col5" >Chanosiast43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row680_col6" class="data row680 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row681" class="row_heading level0 row681" >681</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col0" class="data row681 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col1" class="data row681 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col2" class="data row681 col2" >100</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col3" class="data row681 col3" >Blindscythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col4" class="data row681 col4" >$3.66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col5" class="data row681 col5" >Sundim98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row681_col6" class="data row681 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row682" class="row_heading level0 row682" >682</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col0" class="data row682 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col1" class="data row682 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col2" class="data row682 col2" >83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col3" class="data row682 col3" >Lifebender</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col4" class="data row682 col4" >$3.51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col5" class="data row682 col5" >Frichaya88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row682_col6" class="data row682 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row683" class="row_heading level0 row683" >683</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col0" class="data row683 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col1" class="data row683 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col2" class="data row683 col2" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col3" class="data row683 col3" >Hero Cane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col4" class="data row683 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col5" class="data row683 col5" >Lirtassa47</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row683_col6" class="data row683 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row684" class="row_heading level0 row684" >684</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col0" class="data row684 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col1" class="data row684 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col2" class="data row684 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col3" class="data row684 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col4" class="data row684 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col5" class="data row684 col5" >Iathenudil29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row684_col6" class="data row684 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row685" class="row_heading level0 row685" >685</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col0" class="data row685 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col1" class="data row685 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col2" class="data row685 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col3" class="data row685 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col4" class="data row685 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col5" class="data row685 col5" >Lisirra55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row685_col6" class="data row685 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row686" class="row_heading level0 row686" >686</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col0" class="data row686 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col1" class="data row686 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col2" class="data row686 col2" >46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col3" class="data row686 col3" >Hopeless Ebon Dualblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col4" class="data row686 col4" >$4.75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col5" class="data row686 col5" >Yarolwen77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row686_col6" class="data row686 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row687" class="row_heading level0 row687" >687</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col0" class="data row687 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col1" class="data row687 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col2" class="data row687 col2" >112</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col3" class="data row687 col3" >Worldbreaker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col4" class="data row687 col4" >$3.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col5" class="data row687 col5" >Crausirra42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row687_col6" class="data row687 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row688" class="row_heading level0 row688" >688</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col0" class="data row688 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col1" class="data row688 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col2" class="data row688 col2" >87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col3" class="data row688 col3" >Deluge, Edge of the West</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col4" class="data row688 col4" >$2.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col5" class="data row688 col5" >Frichast72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row688_col6" class="data row688 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row689" class="row_heading level0 row689" >689</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col0" class="data row689 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col1" class="data row689 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col2" class="data row689 col2" >33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col3" class="data row689 col3" >Curved Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col4" class="data row689 col4" >$1.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col5" class="data row689 col5" >Eulidru49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row689_col6" class="data row689 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row690" class="row_heading level0 row690" >690</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col0" class="data row690 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col1" class="data row690 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col2" class="data row690 col2" >81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col3" class="data row690 col3" >Dreamkiss</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col4" class="data row690 col4" >$4.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col5" class="data row690 col5" >Aidain51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row690_col6" class="data row690 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row691" class="row_heading level0 row691" >691</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col0" class="data row691 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col1" class="data row691 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col2" class="data row691 col2" >40</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col3" class="data row691 col3" >Second Chance</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col4" class="data row691 col4" >$2.34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col5" class="data row691 col5" >Sida61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row691_col6" class="data row691 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row692" class="row_heading level0 row692" >692</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col0" class="data row692 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col1" class="data row692 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col2" class="data row692 col2" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col3" class="data row692 col3" >Crucifer</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col4" class="data row692 col4" >$2.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col5" class="data row692 col5" >Chamjasknya65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row692_col6" class="data row692 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row693" class="row_heading level0 row693" >693</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col0" class="data row693 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col1" class="data row693 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col2" class="data row693 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col3" class="data row693 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col4" class="data row693 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col5" class="data row693 col5" >Iri67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row693_col6" class="data row693 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row694" class="row_heading level0 row694" >694</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col0" class="data row694 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col1" class="data row694 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col2" class="data row694 col2" >91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col3" class="data row694 col3" >Celeste</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col4" class="data row694 col4" >$3.71</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col5" class="data row694 col5" >Ririp86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row694_col6" class="data row694 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row695" class="row_heading level0 row695" >695</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col0" class="data row695 col0" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col1" class="data row695 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col2" class="data row695 col2" >117</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col3" class="data row695 col3" >Heartstriker, Legacy of the Light</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col4" class="data row695 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col5" class="data row695 col5" >Chadossa56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row695_col6" class="data row695 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row696" class="row_heading level0 row696" >696</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col0" class="data row696 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col1" class="data row696 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col2" class="data row696 col2" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col3" class="data row696 col3" >Unholy Wand</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col4" class="data row696 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col5" class="data row696 col5" >Chanjaskan89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row696_col6" class="data row696 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row697" class="row_heading level0 row697" >697</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col0" class="data row697 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col1" class="data row697 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col2" class="data row697 col2" >93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col3" class="data row697 col3" >Apocalyptic Battlescythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col4" class="data row697 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col5" class="data row697 col5" >Jiskimsda56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row697_col6" class="data row697 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row698" class="row_heading level0 row698" >698</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col0" class="data row698 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col1" class="data row698 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col2" class="data row698 col2" >66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col3" class="data row698 col3" >Victor Iron Spikes</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col4" class="data row698 col4" >$3.55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col5" class="data row698 col5" >Assistast50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row698_col6" class="data row698 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row699" class="row_heading level0 row699" >699</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col0" class="data row699 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col1" class="data row699 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col2" class="data row699 col2" >162</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col3" class="data row699 col3" >Abyssal Shard</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col4" class="data row699 col4" >$2.04</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col5" class="data row699 col5" >Euliria52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row699_col6" class="data row699 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row700" class="row_heading level0 row700" >700</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col0" class="data row700 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col1" class="data row700 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col2" class="data row700 col2" >43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col3" class="data row700 col3" >Foul Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col4" class="data row700 col4" >$2.38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col5" class="data row700 col5" >Aerithriaphos45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row700_col6" class="data row700 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row701" class="row_heading level0 row701" >701</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col0" class="data row701 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col1" class="data row701 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col2" class="data row701 col2" >170</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col3" class="data row701 col3" >Shadowsteel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col4" class="data row701 col4" >$1.98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col5" class="data row701 col5" >Ila44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row701_col6" class="data row701 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row702" class="row_heading level0 row702" >702</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col0" class="data row702 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col1" class="data row702 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col2" class="data row702 col2" >128</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col3" class="data row702 col3" >Blazeguard, Reach of Eternity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col4" class="data row702 col4" >$4.00</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col5" class="data row702 col5" >Sida61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row702_col6" class="data row702 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row703" class="row_heading level0 row703" >703</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col0" class="data row703 col0" >38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col1" class="data row703 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col2" class="data row703 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col3" class="data row703 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col4" class="data row703 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col5" class="data row703 col5" >Phyali88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row703_col6" class="data row703 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row704" class="row_heading level0 row704" >704</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col0" class="data row704 col0" >30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col1" class="data row704 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col2" class="data row704 col2" >72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col3" class="data row704 col3" >Winter's Bite</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col4" class="data row704 col4" >$1.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col5" class="data row704 col5" >Iskossa88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row704_col6" class="data row704 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row705" class="row_heading level0 row705" >705</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col0" class="data row705 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col1" class="data row705 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col2" class="data row705 col2" >115</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col3" class="data row705 col3" >Spectral Diamond Doomblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col4" class="data row705 col4" >$4.25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col5" class="data row705 col5" >Aeral85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row705_col6" class="data row705 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row706" class="row_heading level0 row706" >706</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col0" class="data row706 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col1" class="data row706 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col2" class="data row706 col2" >61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col3" class="data row706 col3" >Ragnarok</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col4" class="data row706 col4" >$3.97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col5" class="data row706 col5" >Rinallorap73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row706_col6" class="data row706 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row707" class="row_heading level0 row707" >707</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col0" class="data row707 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col1" class="data row707 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col2" class="data row707 col2" >5</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col3" class="data row707 col3" >Putrid Fan</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col4" class="data row707 col4" >$1.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col5" class="data row707 col5" >Chanjask65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row707_col6" class="data row707 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row708" class="row_heading level0 row708" >708</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col0" class="data row708 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col1" class="data row708 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col2" class="data row708 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col3" class="data row708 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col4" class="data row708 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col5" class="data row708 col5" >Saedue76</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row708_col6" class="data row708 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row709" class="row_heading level0 row709" >709</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col0" class="data row709 col0" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col1" class="data row709 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col2" class="data row709 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col3" class="data row709 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col4" class="data row709 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col5" class="data row709 col5" >Assassa38</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row709_col6" class="data row709 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row710" class="row_heading level0 row710" >710</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col0" class="data row710 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col1" class="data row710 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col2" class="data row710 col2" >67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col3" class="data row710 col3" >Celeste, Incarnation of the Corrupted</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col4" class="data row710 col4" >$2.31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col5" class="data row710 col5" >Tyaelorgue39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row710_col6" class="data row710 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row711" class="row_heading level0 row711" >711</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col0" class="data row711 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col1" class="data row711 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col2" class="data row711 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col3" class="data row711 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col4" class="data row711 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col5" class="data row711 col5" >Tyananurgue44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row711_col6" class="data row711 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row712" class="row_heading level0 row712" >712</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col0" class="data row712 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col1" class="data row712 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col2" class="data row712 col2" >5</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col3" class="data row712 col3" >Putrid Fan</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col4" class="data row712 col4" >$1.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col5" class="data row712 col5" >Isketo41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row712_col6" class="data row712 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row713" class="row_heading level0 row713" >713</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col0" class="data row713 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col1" class="data row713 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col2" class="data row713 col2" >159</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col3" class="data row713 col3" >Oathbreaker, Spellblade of Trials</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col4" class="data row713 col4" >$3.01</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col5" class="data row713 col5" >Sundast87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row713_col6" class="data row713 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row714" class="row_heading level0 row714" >714</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col0" class="data row714 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col1" class="data row714 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col2" class="data row714 col2" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col3" class="data row714 col3" >Shadow Strike, Glory of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col4" class="data row714 col4" >$1.93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col5" class="data row714 col5" >Yadacal26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row714_col6" class="data row714 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row715" class="row_heading level0 row715" >715</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col0" class="data row715 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col1" class="data row715 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col2" class="data row715 col2" >174</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col3" class="data row715 col3" >Primitive Blade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col4" class="data row715 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col5" class="data row715 col5" >Ila44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row715_col6" class="data row715 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row716" class="row_heading level0 row716" >716</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col0" class="data row716 col0" >9</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col1" class="data row716 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col2" class="data row716 col2" >103</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col3" class="data row716 col3" >Singed Scalpel</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col4" class="data row716 col4" >$4.87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col5" class="data row716 col5" >Ilophos58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row716_col6" class="data row716 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row717" class="row_heading level0 row717" >717</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col0" class="data row717 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col1" class="data row717 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col2" class="data row717 col2" >102</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col3" class="data row717 col3" >Avenger</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col4" class="data row717 col4" >$4.16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col5" class="data row717 col5" >Marilsanya48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row717_col6" class="data row717 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row718" class="row_heading level0 row718" >718</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col0" class="data row718 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col1" class="data row718 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col2" class="data row718 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col3" class="data row718 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col4" class="data row718 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col5" class="data row718 col5" >Phially37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row718_col6" class="data row718 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row719" class="row_heading level0 row719" >719</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col0" class="data row719 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col1" class="data row719 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col2" class="data row719 col2" >169</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col3" class="data row719 col3" >Interrogator, Blood Blade of the Queen</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col4" class="data row719 col4" >$3.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col5" class="data row719 col5" >Iduedru67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row719_col6" class="data row719 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row720" class="row_heading level0 row720" >720</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col0" class="data row720 col0" >7</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col1" class="data row720 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col2" class="data row720 col2" >82</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col3" class="data row720 col3" >Nirvana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col4" class="data row720 col4" >$1.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col5" class="data row720 col5" >Yarithsurgue62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row720_col6" class="data row720 col6" >Less than 10</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row721" class="row_heading level0 row721" >721</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col0" class="data row721 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col1" class="data row721 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col2" class="data row721 col2" >39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col3" class="data row721 col3" >Betrayal, Whisper of Grieving Widows</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col4" class="data row721 col4" >$2.35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col5" class="data row721 col5" >Aeduera68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row721_col6" class="data row721 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row722" class="row_heading level0 row722" >722</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col0" class="data row722 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col1" class="data row722 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col2" class="data row722 col2" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col3" class="data row722 col3" >Torchlight, Bond of Storms</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col4" class="data row722 col4" >$1.77</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col5" class="data row722 col5" >Saidairiaphos61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row722_col6" class="data row722 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row723" class="row_heading level0 row723" >723</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col0" class="data row723 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col1" class="data row723 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col2" class="data row723 col2" >69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col3" class="data row723 col3" >Frenzy, Defender of the Harvest</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col4" class="data row723 col4" >$1.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col5" class="data row723 col5" >Tillyrin30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row723_col6" class="data row723 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row724" class="row_heading level0 row724" >724</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col0" class="data row724 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col1" class="data row724 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col2" class="data row724 col2" >117</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col3" class="data row724 col3" >Heartstriker, Legacy of the Light</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col4" class="data row724 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col5" class="data row724 col5" >Chanosiast43</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row724_col6" class="data row724 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row725" class="row_heading level0 row725" >725</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col0" class="data row725 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col1" class="data row725 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col2" class="data row725 col2" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col3" class="data row725 col3" >Possessed Core</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col4" class="data row725 col4" >$1.59</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col5" class="data row725 col5" >Quarusrion32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row725_col6" class="data row725 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row726" class="row_heading level0 row726" >726</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col0" class="data row726 col0" >18</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col1" class="data row726 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col2" class="data row726 col2" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col3" class="data row726 col3" >Souleater</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col4" class="data row726 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col5" class="data row726 col5" >Chamimla73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row726_col6" class="data row726 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row727" class="row_heading level0 row727" >727</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col0" class="data row727 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col1" class="data row727 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col2" class="data row727 col2" >139</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col3" class="data row727 col3" >Mercy, Katana of Dismay</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col4" class="data row727 col4" >$4.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col5" class="data row727 col5" >Eurith26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row727_col6" class="data row727 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row728" class="row_heading level0 row728" >728</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col0" class="data row728 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col1" class="data row728 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col2" class="data row728 col2" >48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col3" class="data row728 col3" >Rage, Legacy of the Lone Victor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col4" class="data row728 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col5" class="data row728 col5" >Tyananurgue44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row728_col6" class="data row728 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row729" class="row_heading level0 row729" >729</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col0" class="data row729 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col1" class="data row729 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col2" class="data row729 col2" >134</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col3" class="data row729 col3" >Undead Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col4" class="data row729 col4" >$4.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col5" class="data row729 col5" >Iskichinya81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row729_col6" class="data row729 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row730" class="row_heading level0 row730" >730</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col0" class="data row730 col0" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col1" class="data row730 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col2" class="data row730 col2" >148</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col3" class="data row730 col3" >Warmonger, Gift of Suffering's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col4" class="data row730 col4" >$3.96</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col5" class="data row730 col5" >Hiadanurin36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row730_col6" class="data row730 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row731" class="row_heading level0 row731" >731</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col0" class="data row731 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col1" class="data row731 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col2" class="data row731 col2" >106</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col3" class="data row731 col3" >Crying Steel Sickle</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col4" class="data row731 col4" >$2.29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col5" class="data row731 col5" >Tyaelly53</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row731_col6" class="data row731 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row732" class="row_heading level0 row732" >732</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col0" class="data row732 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col1" class="data row732 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col2" class="data row732 col2" >37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col3" class="data row732 col3" >Shadow Strike, Glory of Ending Hope</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col4" class="data row732 col4" >$1.93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col5" class="data row732 col5" >Shidai42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row732_col6" class="data row732 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row733" class="row_heading level0 row733" >733</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col0" class="data row733 col0" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col1" class="data row733 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col2" class="data row733 col2" >8</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col3" class="data row733 col3" >Purgatory, Gem of Regret</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col4" class="data row733 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col5" class="data row733 col5" >Bartassaya73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row733_col6" class="data row733 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row734" class="row_heading level0 row734" >734</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col0" class="data row734 col0" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col1" class="data row734 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col2" class="data row734 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col3" class="data row734 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col4" class="data row734 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col5" class="data row734 col5" >Mindosiasya28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row734_col6" class="data row734 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row735" class="row_heading level0 row735" >735</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col0" class="data row735 col0" >10</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col1" class="data row735 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col2" class="data row735 col2" >16</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col3" class="data row735 col3" >Restored Bauble</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col4" class="data row735 col4" >$3.11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col5" class="data row735 col5" >Ethrusuard41</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row735_col6" class="data row735 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row736" class="row_heading level0 row736" >736</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col0" class="data row736 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col1" class="data row736 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col2" class="data row736 col2" >45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col3" class="data row736 col3" >Glinting Glass Edge</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col4" class="data row736 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col5" class="data row736 col5" >Indirrian56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row736_col6" class="data row736 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row737" class="row_heading level0 row737" >737</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col0" class="data row737 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col1" class="data row737 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col2" class="data row737 col2" >101</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col3" class="data row737 col3" >Final Critic</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col4" class="data row737 col4" >$4.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col5" class="data row737 col5" >Sondim68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row737_col6" class="data row737 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row738" class="row_heading level0 row738" >738</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col0" class="data row738 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col1" class="data row738 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col2" class="data row738 col2" >56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col3" class="data row738 col3" >Foul Titanium Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col4" class="data row738 col4" >$4.33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col5" class="data row738 col5" >Tyadaru49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row738_col6" class="data row738 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row739" class="row_heading level0 row739" >739</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col0" class="data row739 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col1" class="data row739 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col2" class="data row739 col2" >93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col3" class="data row739 col3" >Apocalyptic Battlescythe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col4" class="data row739 col4" >$3.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col5" class="data row739 col5" >Cosadar58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row739_col6" class="data row739 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row740" class="row_heading level0 row740" >740</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col0" class="data row740 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col1" class="data row740 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col2" class="data row740 col2" >154</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col3" class="data row740 col3" >Feral Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col4" class="data row740 col4" >$2.19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col5" class="data row740 col5" >Farusrian86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row740_col6" class="data row740 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row741" class="row_heading level0 row741" >741</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col0" class="data row741 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col1" class="data row741 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col2" class="data row741 col2" >145</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col3" class="data row741 col3" >Fiery Glass Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col4" class="data row741 col4" >$4.45</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col5" class="data row741 col5" >Leyirra83</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row741_col6" class="data row741 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row742" class="row_heading level0 row742" >742</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col0" class="data row742 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col1" class="data row742 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col2" class="data row742 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col3" class="data row742 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col4" class="data row742 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col5" class="data row742 col5" >Inguron55</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row742_col6" class="data row742 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row743" class="row_heading level0 row743" >743</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col0" class="data row743 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col1" class="data row743 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col2" class="data row743 col2" >134</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col3" class="data row743 col3" >Undead Crusader</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col4" class="data row743 col4" >$4.67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col5" class="data row743 col5" >Haedasu65</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row743_col6" class="data row743 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row744" class="row_heading level0 row744" >744</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col0" class="data row744 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col1" class="data row744 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col2" class="data row744 col2" >130</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col3" class="data row744 col3" >Alpha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col4" class="data row744 col4" >$1.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col5" class="data row744 col5" >Ialistidru50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row744_col6" class="data row744 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row745" class="row_heading level0 row745" >745</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col0" class="data row745 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col1" class="data row745 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col2" class="data row745 col2" >79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col3" class="data row745 col3" >Alpha, Oath of Zeal</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col4" class="data row745 col4" >$2.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col5" class="data row745 col5" >Sweecossa42</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row745_col6" class="data row745 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row746" class="row_heading level0 row746" >746</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col0" class="data row746 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col1" class="data row746 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col2" class="data row746 col2" >34</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col3" class="data row746 col3" >Retribution Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col4" class="data row746 col4" >$4.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col5" class="data row746 col5" >Ralasti48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row746_col6" class="data row746 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row747" class="row_heading level0 row747" >747</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col0" class="data row747 col0" >32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col1" class="data row747 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col2" class="data row747 col2" >52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col3" class="data row747 col3" >Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col4" class="data row747 col4" >$4.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col5" class="data row747 col5" >Lamon28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row747_col6" class="data row747 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row748" class="row_heading level0 row748" >748</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col0" class="data row748 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col1" class="data row748 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col2" class="data row748 col2" >120</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col3" class="data row748 col3" >Agatha</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col4" class="data row748 col4" >$1.91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col5" class="data row748 col5" >Isri49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row748_col6" class="data row748 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row749" class="row_heading level0 row749" >749</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col0" class="data row749 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col1" class="data row749 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col2" class="data row749 col2" >114</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col3" class="data row749 col3" >Yearning Mageblade</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col4" class="data row749 col4" >$1.79</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col5" class="data row749 col5" >Frichassala85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row749_col6" class="data row749 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row750" class="row_heading level0 row750" >750</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col0" class="data row750 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col1" class="data row750 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col2" class="data row750 col2" >86</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col3" class="data row750 col3" >Stormfury Lantern</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col4" class="data row750 col4" >$1.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col5" class="data row750 col5" >Eollym91</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row750_col6" class="data row750 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row751" class="row_heading level0 row751" >751</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col0" class="data row751 col0" >26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col1" class="data row751 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col2" class="data row751 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col3" class="data row751 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col4" class="data row751 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col5" class="data row751 col5" >Lisjasksda68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row751_col6" class="data row751 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row752" class="row_heading level0 row752" >752</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col0" class="data row752 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col1" class="data row752 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col2" class="data row752 col2" >116</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col3" class="data row752 col3" >Renewed Skeletal Katana</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col4" class="data row752 col4" >$2.37</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col5" class="data row752 col5" >Yalostiphos68</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row752_col6" class="data row752 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row753" class="row_heading level0 row753" >753</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col0" class="data row753 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col1" class="data row753 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col2" class="data row753 col2" >4</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col3" class="data row753 col3" >Bloodlord's Fetish</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col4" class="data row753 col4" >$2.28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col5" class="data row753 col5" >Thryallym62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row753_col6" class="data row753 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row754" class="row_heading level0 row754" >754</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col0" class="data row754 col0" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col1" class="data row754 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col2" class="data row754 col2" >104</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col3" class="data row754 col3" >Gladiator's Glaive</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col4" class="data row754 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col5" class="data row754 col5" >Sondastan54</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row754_col6" class="data row754 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row755" class="row_heading level0 row755" >755</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col0" class="data row755 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col1" class="data row755 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col2" class="data row755 col2" >179</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col3" class="data row755 col3" >Wolf, Promise of the Moonwalker</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col4" class="data row755 col4" >$1.88</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col5" class="data row755 col5" >Ailaesuir66</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row755_col6" class="data row755 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row756" class="row_heading level0 row756" >756</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col0" class="data row756 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col1" class="data row756 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col2" class="data row756 col2" >6</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col3" class="data row756 col3" >Rusty Skull</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col4" class="data row756 col4" >$1.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col5" class="data row756 col5" >Siasri67</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row756_col6" class="data row756 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row757" class="row_heading level0 row757" >757</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col0" class="data row757 col0" >35</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col1" class="data row757 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col2" class="data row757 col2" >11</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col3" class="data row757 col3" >Brimstone</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col4" class="data row757 col4" >$2.52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col5" class="data row757 col5" >Seosri62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row757_col6" class="data row757 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row758" class="row_heading level0 row758" >758</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col0" class="data row758 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col1" class="data row758 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col2" class="data row758 col2" >122</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col3" class="data row758 col3" >Unending Tyranny</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col4" class="data row758 col4" >$1.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col5" class="data row758 col5" >Ryastycal90</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row758_col6" class="data row758 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row759" class="row_heading level0 row759" >759</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col0" class="data row759 col0" >19</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col1" class="data row759 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col2" class="data row759 col2" >87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col3" class="data row759 col3" >Deluge, Edge of the West</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col4" class="data row759 col4" >$2.20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col5" class="data row759 col5" >Chanirrasta87</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row759_col6" class="data row759 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row760" class="row_heading level0 row760" >760</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col0" class="data row760 col0" >29</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col1" class="data row760 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col2" class="data row760 col2" >81</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col3" class="data row760 col3" >Dreamkiss</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col4" class="data row760 col4" >$4.06</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col5" class="data row760 col5" >Aerithllora36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row760_col6" class="data row760 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row761" class="row_heading level0 row761" >761</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col0" class="data row761 col0" >28</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col1" class="data row761 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col2" class="data row761 col2" >175</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col3" class="data row761 col3" >Woeful Adamantite Claymore</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col4" class="data row761 col4" >$1.24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col5" class="data row761 col5" >Raeduerin33</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row761_col6" class="data row761 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row762" class="row_heading level0 row762" >762</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col0" class="data row762 col0" >36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col1" class="data row762 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col2" class="data row762 col2" >52</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col3" class="data row762 col3" >Hatred</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col4" class="data row762 col4" >$4.39</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col5" class="data row762 col5" >Lisosiast26</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row762_col6" class="data row762 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row763" class="row_heading level0 row763" >763</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col0" class="data row763 col0" >27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col1" class="data row763 col1" >Other / Non-Disclosed</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col2" class="data row763 col2" >48</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col3" class="data row763 col3" >Rage, Legacy of the Lone Victor</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col4" class="data row763 col4" >$4.32</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col5" class="data row763 col5" >Eurisuru25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row763_col6" class="data row763 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row764" class="row_heading level0 row764" >764</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col0" class="data row764 col0" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col1" class="data row764 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col2" class="data row764 col2" >70</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col3" class="data row764 col3" >Hope's End</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col4" class="data row764 col4" >$3.89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col5" class="data row764 col5" >Assassasda84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row764_col6" class="data row764 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row765" class="row_heading level0 row765" >765</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col0" class="data row765 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col1" class="data row765 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col2" class="data row765 col2" >13</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col3" class="data row765 col3" >Serenity</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col4" class="data row765 col4" >$1.49</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col5" class="data row765 col5" >Aerithnucal56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row765_col6" class="data row765 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row766" class="row_heading level0 row766" >766</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col0" class="data row766 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col1" class="data row766 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col2" class="data row766 col2" >84</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col3" class="data row766 col3" >Arcane Gem</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col4" class="data row766 col4" >$2.23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col5" class="data row766 col5" >Nitherian58</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row766_col6" class="data row766 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row767" class="row_heading level0 row767" >767</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col0" class="data row767 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col1" class="data row767 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col2" class="data row767 col2" >122</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col3" class="data row767 col3" >Unending Tyranny</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col4" class="data row767 col4" >$1.21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col5" class="data row767 col5" >Hailaphos89</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row767_col6" class="data row767 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row768" class="row_heading level0 row768" >768</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col0" class="data row768 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col1" class="data row768 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col2" class="data row768 col2" >158</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col3" class="data row768 col3" >Darkheart, Butcher of the Champion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col4" class="data row768 col4" >$3.56</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col5" class="data row768 col5" >Chamucosda93</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row768_col6" class="data row768 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row769" class="row_heading level0 row769" >769</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col0" class="data row769 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col1" class="data row769 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col2" class="data row769 col2" >73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col3" class="data row769 col3" >Ritual Mace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col4" class="data row769 col4" >$3.74</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col5" class="data row769 col5" >Frichilsasya78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row769_col6" class="data row769 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row770" class="row_heading level0 row770" >770</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col0" class="data row770 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col1" class="data row770 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col2" class="data row770 col2" >141</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col3" class="data row770 col3" >Persuasion</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col4" class="data row770 col4" >$3.27</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col5" class="data row770 col5" >Aenasu69</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row770_col6" class="data row770 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row771" class="row_heading level0 row771" >771</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col0" class="data row771 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col1" class="data row771 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col2" class="data row771 col2" >25</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col3" class="data row771 col3" >Hero Cane</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col4" class="data row771 col4" >$1.03</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col5" class="data row771 col5" >Lassista97</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row771_col6" class="data row771 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row772" class="row_heading level0 row772" >772</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col0" class="data row772 col0" >15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col1" class="data row772 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col2" class="data row772 col2" >31</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col3" class="data row772 col3" >Trickster</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col4" class="data row772 col4" >$2.07</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col5" class="data row772 col5" >Sidap51</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row772_col6" class="data row772 col6" >Between 15 to 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row773" class="row_heading level0 row773" >773</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col0" class="data row773 col0" >21</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col1" class="data row773 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col2" class="data row773 col2" >44</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col3" class="data row773 col3" >Bonecarvin Battle Axe</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col4" class="data row773 col4" >$2.46</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col5" class="data row773 col5" >Chamadarsda63</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row773_col6" class="data row773 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row774" class="row_heading level0 row774" >774</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col0" class="data row774 col0" >24</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col1" class="data row774 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col2" class="data row774 col2" >123</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col3" class="data row774 col3" >Twilight's Carver</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col4" class="data row774 col4" >$1.14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col5" class="data row774 col5" >Lassassast73</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row774_col6" class="data row774 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row775" class="row_heading level0 row775" >775</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col0" class="data row775 col0" >22</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col1" class="data row775 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col2" class="data row775 col2" >98</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col3" class="data row775 col3" >Deadline, Voice Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col4" class="data row775 col4" >$3.62</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col5" class="data row775 col5" >Eural50</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row775_col6" class="data row775 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row776" class="row_heading level0 row776" >776</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col0" class="data row776 col0" >14</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col1" class="data row776 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col2" class="data row776 col2" >104</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col3" class="data row776 col3" >Gladiator's Glaive</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col4" class="data row776 col4" >$1.36</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col5" class="data row776 col5" >Lirtossa78</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row776_col6" class="data row776 col6" >Between 10 to 15</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row777" class="row_heading level0 row777" >777</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col0" class="data row777 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col1" class="data row777 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col2" class="data row777 col2" >117</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col3" class="data row777 col3" >Heartstriker, Legacy of the Light</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col4" class="data row777 col4" >$4.15</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col5" class="data row777 col5" >Tillyrin30</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row777_col6" class="data row777 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row778" class="row_heading level0 row778" >778</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col0" class="data row778 col0" >20</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col1" class="data row778 col1" >Male</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col2" class="data row778 col2" >75</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col3" class="data row778 col3" >Brutality Ivory Warmace</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col4" class="data row778 col4" >$1.72</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col5" class="data row778 col5" >Quelaton80</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row778_col6" class="data row778 col6" >Greater than 20</td> 
    </tr>    <tr> 
        <th id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7level0_row779" class="row_heading level0 row779" >779</th> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col0" class="data row779 col0" >23</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col1" class="data row779 col1" >Female</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col2" class="data row779 col2" >107</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col3" class="data row779 col3" >Splitter, Foe Of Subtlety</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col4" class="data row779 col4" >$3.61</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col5" class="data row779 col5" >Alim85</td> 
        <td id="T_1133ed1e_28c3_11e8_aa47_8c85905c07d7row779_col6" class="data row779 col6" >Greater than 20</td> 
    </tr></tbody> 
</table> 




```python
# creating a new dataframe for each age range
purchase_data_10_df = purchase_data_df.loc[purchase_data_df["Age Demographics"] == "Less than 10"]
purchase_data_15_df = purchase_data_df.loc[purchase_data_df["Age Demographics"] == "Between 10 to 15"]
purchase_data_20_df = purchase_data_df.loc[purchase_data_df["Age Demographics"] == "Between 15 to 20"]
purchase_data_20_plus_df = purchase_data_df.loc[purchase_data_df["Age Demographics"] == "Greater than 20"]
```


```python
#Counting the length of each data frame to get number of players for each player
purchase_10_count = len(purchase_data_10_df)
purchase_15_count = len(purchase_data_15_df)
purchase_20_count = len(purchase_data_20_df)
purchase_20_plus_count = len(purchase_data_20_plus_df)
```


```python
#Calculating the average price for each age range data frame by using mean function
purchase_10_avgprice = purchase_data_10_df["Price"].mean()
purchase_15_avgprice = purchase_data_15_df["Price"].mean()
purchase_20_avgprice = purchase_data_20_df["Price"].mean()
purchase_20_plus_avgprice = purchase_data_20_plus_df["Price"].mean()
```


```python
# calculating the total purchase value made by each age group
purchase_10_value = purchase_data_10_df["Price"].sum()
purchase_15_value = purchase_data_15_df["Price"].sum()
purchase_20_value = purchase_data_20_df["Price"].sum()
purchase_20_plus_value = purchase_data_20_plus_df["Price"].sum()
```


```python
# putting all together in the new data frame called age demographics
age_demographics_df = pd.DataFrame({"Age Range": ["Less than 10","Between 10 to 15","Between 15 to 20", "Greater than 20"],
                                   "Purchase Count":[purchase_10_count,purchase_15_count,purchase_20_count,purchase_20_plus_count],
                                   "Average Purchase Price":[purchase_10_avgprice,purchase_15_avgprice,purchase_20_avgprice,purchase_20_plus_avgprice],
                                    "Total purchase Value":[purchase_10_value,purchase_15_value,purchase_20_value,purchase_20_plus_value]},
                                  columns = ["Age Range","Purchase Count","Average Purchase Price","Total purchase Value"])
age_demographics_df.style.format({"Average Purchase Price":"${:,.2f}","Total purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_115a5794_28c3_11e8_914a_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Age Range</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Total purchase Value</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_115a5794_28c3_11e8_914a_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row0_col0" class="data row0 col0" >Less than 10</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row0_col1" class="data row0 col1" >28</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row0_col2" class="data row0 col2" >$2.98</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row0_col3" class="data row0 col3" >$83.46</td> 
    </tr>    <tr> 
        <th id="T_115a5794_28c3_11e8_914a_8c85905c07d7level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row1_col0" class="data row1 col0" >Between 10 to 15</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row1_col1" class="data row1 col1" >35</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row1_col2" class="data row1 col2" >$2.77</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row1_col3" class="data row1 col3" >$96.95</td> 
    </tr>    <tr> 
        <th id="T_115a5794_28c3_11e8_914a_8c85905c07d7level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row2_col0" class="data row2 col0" >Between 15 to 20</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row2_col1" class="data row2 col1" >133</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row2_col2" class="data row2 col2" >$2.91</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row2_col3" class="data row2 col3" >$386.42</td> 
    </tr>    <tr> 
        <th id="T_115a5794_28c3_11e8_914a_8c85905c07d7level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row3_col0" class="data row3 col0" >Greater than 20</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row3_col1" class="data row3 col1" >584</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row3_col2" class="data row3 col2" >$2.94</td> 
        <td id="T_115a5794_28c3_11e8_914a_8c85905c07d7row3_col3" class="data row3 col3" >$1,719.50</td> 
    </tr></tbody> 
</table> 




```python
# using the mimmax scaler method to ind the normalized value
age_values = age_demographics_df[["Total purchase Value"]].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
normalized_age_values = min_max_scaler.fit_transform(age_values) #stored normalized value in an array

# creating a new data frame with normalized value
normalized_age_demographics_df = pd.DataFrame({"Age Range": ["Less than 10","Between 10 to 15","Between 15 to 20", "Greater than 20"],
                                   "Purchase Count":[purchase_10_count,purchase_15_count,purchase_20_count,purchase_20_plus_count],
                                   "Average Purchase Price":[purchase_10_avgprice,purchase_15_avgprice,purchase_20_avgprice,purchase_20_plus_avgprice],
                                    "Total purchase Value":[purchase_10_value,purchase_15_value,purchase_20_value,purchase_20_plus_value],
                                    "Normalized Total Purchase Values":[normalized_age_values[0],normalized_age_values[1],normalized_age_values[2],normalized_age_values[3]]})
normalized_age_demographics_df.style.format({"Average Purchase Price":"${:,.2f}","Total purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Age Range</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Normalized Total Purchase Values</th> 
        <th class="col_heading level0 col3" >Purchase Count</th> 
        <th class="col_heading level0 col4" >Total purchase Value</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row0_col0" class="data row0 col0" >Less than 10</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row0_col1" class="data row0 col1" >$2.98</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row0_col2" class="data row0 col2" >[0.]</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row0_col3" class="data row0 col3" >28</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row0_col4" class="data row0 col4" >$83.46</td> 
    </tr>    <tr> 
        <th id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row1_col0" class="data row1 col0" >Between 10 to 15</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row1_col1" class="data row1 col1" >$2.77</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row1_col2" class="data row1 col2" >[0.00824552]</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row1_col3" class="data row1 col3" >35</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row1_col4" class="data row1 col4" >$96.95</td> 
    </tr>    <tr> 
        <th id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row2_col0" class="data row2 col0" >Between 15 to 20</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row2_col1" class="data row2 col1" >$2.91</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row2_col2" class="data row2 col2" >[0.18517885]</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row2_col3" class="data row2 col3" >133</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row2_col4" class="data row2 col4" >$386.42</td> 
    </tr>    <tr> 
        <th id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row3_col0" class="data row3 col0" >Greater than 20</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row3_col1" class="data row3 col1" >$2.94</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row3_col2" class="data row3 col2" >[1.]</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row3_col3" class="data row3 col3" >584</td> 
        <td id="T_115cdda2_28c3_11e8_ae58_8c85905c07d7row3_col4" class="data row3 col4" >$1,719.50</td> 
    </tr></tbody> 
</table> 



#### Top 5 Spenders


```python
# Logic to calculate the top spenders.
spenders_df = purchase_data_df.groupby("SN") # grouped by SN to get the unique players
spenders_purchase_count = spenders_df["SN"].count() #Getting the number of spenders per SN
spenders_avgprice = spenders_df["Price"].mean()  #geting mean for each palyer purchase
spenders_value = spenders_df["Price"].sum()#getting how much a player spent

#Creating a new data fram to put all the values together
top_spenders_df = pd.DataFrame({"Purchase count":spenders_purchase_count,
                               "Average Price": spenders_avgprice,
                               "Total Purchase Value":spenders_value})

top_spenders_df["Total Purchase Value"] = top_spenders_df["Total Purchase Value"].map('${:,.2f}'.format)
top_spenders_df["Average Price"] = top_spenders_df["Average Price"].map('${:,.2f}'.format)

top_spenders_df.sort_values("Purchase count",ascending = False).head() # sorting the DF to get the most purchased count by player so that we can know who spent most

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Purchase count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$3.41</td>
      <td>5</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$3.18</td>
      <td>4</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Qarwen67</th>
      <td>$2.49</td>
      <td>4</td>
      <td>$9.97</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$3.39</td>
      <td>4</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Sondastan54</th>
      <td>$2.56</td>
      <td>4</td>
      <td>$10.24</td>
    </tr>
  </tbody>
</table>
</div>



#### Top 5 Popular Items


```python
#calculating the popular item bu groupig the original data frame by Item ID and name
popular_df = purchase_data_df.groupby(["Item ID","Item Name"])
popular_purchase_count = popular_df["Price"].count()
popular_value = popular_df["Price"].sum()
popular_price = popular_df["Price"].unique()


popular_items_df = pd.DataFrame({"Purchase count":popular_purchase_count,
                               "Total Purchase Value":popular_value,
                                "Price":popular_price})


most_popular_items_df = popular_items_df.sort_values("Purchase count",ascending = False) # sorting the DF in descending order to get the most purchase count to see most purchased item
price_temp = most_popular_items_df["Price"].astype(float)
most_popular_items_df["Price"] = price_temp
most_popular_items_df["Total Purchase Value"] = most_popular_items_df["Total Purchase Value"].map("${:.2f}".format)
most_popular_items_df["Price"] = most_popular_items_df["Price"].map("${:.2f}".format)
most_popular_items_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Price</th>
      <th>Purchase count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>$2.35</td>
      <td>11</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>$2.23</td>
      <td>11</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>$2.07</td>
      <td>9</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>$1.24</td>
      <td>9</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>$1.49</td>
      <td>9</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>



#### Top 5 Profitable Items


```python
# used the same data frame and sorted descending using the total purchased value to find the most profitable item
most_profitable_item_df = popular_items_df.sort_values("Total Purchase Value",ascending = False)
price_temp_1= most_profitable_item_df["Price"].astype(float)
most_profitable_item_df["Price"] = price_temp
most_profitable_item_df["Total Purchase Value"] = most_profitable_item_df["Total Purchase Value"].map("${:.2f}".format)
most_profitable_item_df["Price"] = most_profitable_item_df["Price"].map("${:.2f}".format)
most_profitable_item_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Price</th>
      <th>Purchase count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>$4.25</td>
      <td>7</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>$4.95</td>
      <td>6</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>$4.87</td>
      <td>6</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>$3.61</td>
      <td>8</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


