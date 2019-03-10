groupby
-------------

reference: https://pandas.pydata.org/pandas-docs/stable/groupby.html

using "groupby" usually involves one or more of the these steps: 
splitting, applying a function and combining the results.

e.g.  
```
>>> b = np.array( [ [1,2,3], [4,5,6], [1, 3, 3], [4,2,2] ] )
>>> bp = pd.DataFrame(b)
>>> bp.columns = ['b1', 'b2', 'b3']
>>> bp.groupby(['b1'])
<pandas.core.groupby.DataFrameGroupBy object at 0x7f9d73423550>
>>> bp.groupby(['b1']).mean()
     b2   b3
b1          
1   2.5  3.0
4   3.5  4.0
```

the above examples shows based on column 'b1', the rows when b1==1 are grouped together and mean is computed.
and similar for the rows when b1 == 4.

groupby.py provides a better example.
