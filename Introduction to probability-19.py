## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags[flags['bars'] == flags['bars'].max()]['name'] 
highest_population_country = flags[flags['population'] == flags['population'].max()]['name'] 

## 2. Calculating probability ##

total_countries = flags.shape[0]

flags[['colors','stripes']].head()
orange_count = flags[flags['orange'] == 1 ].shape[0]

orange_probability = orange_count / total_countries
stripe = flags[flags['stripes'] > 1 ].shape[0]
stripe_probability = stripe / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10

hundred_heads = .5 **100


## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.

red = flags[flags['red']==1].shape[0]

toatl = flags.shape[0]

three_red =  (red/toatl  ) * ((red-1) /(toatl-1)) * ((red-2)/(toatl-2))

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_count =0 
seventy = 0 
for i in range(start,end+1):
    if ( i % 100 == 0) :
        hundred_count= hundred_count +1
    if ( i % 70 == 0) :    
        seventy = seventy +1
        
hundred_prob =  hundred_count / (len( range(start,end)) +1)
seventy_prob  =  seventy /( len( range(start,end)) +1)

print(len( range(start,end)) )

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / flags.shape[0]
orange = flags[flags["orange"] == 1].shape[0] / flags.shape[0]
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / flags.shape[0]

red_or_orange = red + orange - red_and_orange

stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
all_three_tails = (1/2 * 1/2 * 1/2)
heads_or = 1 - all_three_tails