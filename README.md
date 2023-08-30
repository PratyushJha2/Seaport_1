# Seaport_1
Answering some questions about seaports via a dataset about seaports (WiP)

![image](https://github.com/PratyushJha2/Seaport_1/assets/141875955/d4228316-aa64-4a32-b5ba-a37f53486bfa)

(Pictured: Aerial view of the Port of Shanghai, the largest container port in the world)

I was scrolling through Kaggle for some fun datasets and fate handed me this one about seaports. 

They're not something people usually think about as people typically don't use a cargo ship
to enjoy their upcoming vacation somewhere on the other side of the big local ocean. And yet, 76% of all trade and 90% of international trade utilizes
some form of marine transportation, amounting to $1.5 Trillion dollars worth of goods moving in and out of US ports alone! Where I live (NJ) residents are
largely familiar with the industrial wasteland north of Exit 13 on the New Jersey Turnpike (I-95), mostly because of its uniquely horrid smells (yes, plural) and unsightly views, consisting 
of oil/gas refineries, power plants, and the East Coast's most important seaport (Port Newark). 

![image](https://github.com/PratyushJha2/Seaport_1/assets/141875955/2121984f-0c82-49a2-a07d-f9854c6094cb)

Tashka, via CanStock

(Who can smell this picture?)

I decided to see what kind of fun stuff I can do with this dataset, and that desire has manifested in this project.

According to the NOAA, the volume of traffic for marine ports approximately doubled in 2021 and is forecasted to double again shortly after 2030. The increased
traffic seaports will be expected to deal with, along the global focus on reducing carbon emissions (cargo ships are notoriously bad emitters) means that engineers
and scientists will be tasked to optimize traffic flows and carbon emissions into and out of seaports. While that would require more volatile, sensititve data 
held by various port authorities and governments, there are some interesting and important questions we can answer with the data provided to the everyday internet 
surfer/ameteur programmer interested in cool graphs (namely me). This project focuses on the 500 biggest seaports in the world (for reference, there are approximately 800 active seaports in the world, with the
top 50 making up over half of global trade). 

  - In what countries are the worlds 500 biggest seaports located? (I know my long winded rave of seaports was US-Centric and a bit exclusive to my home, but other areas around the world
    also utilize seaports (who knew??))
    - And in what global regions do they reside, in addition to which countries?
  - How are total number of vessels in port related to arrivals and departures? And how are those latter two related?
  - What is the most 'average' of the top 500 ports, in terms of vessels in port, arrivals/departures, geographical epicenter and name?

To answer these questions, I can make various visualizations in Seaborn and Plotly libraries to draw conclusions about how certain
metrics are related. In addition, I can utilize a least squares method (OLS) to provide a more mathematical, dare I say "nerdy" conclusion about the data. 

If anyone has any possible contributions or advice for this project, I would really (really!) appreciate any input or criticism at all because I am still a 
little new to this kind of thing. 


Sources:

Dataset: https://www.kaggle.com/datasets/sanjeetsinghnaik/ship-ports

Exit 13A Picture: https://cdn.w600.comps.canstockphoto.com/nj-turnpike-stock-photograph_csp1046819.jpg

Shanghai Port Picture: https://www.shlingang.com/en/lingangjituan/xwzx/jtdt/202106/t20210628_22526.shtml

Facts & Figures:
- https://moverdb.com/top-49-container-ports/#:~:text=There%20are%20thousands%20of%20freight,takes%20place%20over%20the%20waves.
- https://coast.noaa.gov/states/fast-facts/ports.html#:~:text=76%25%20of%20Trade,90%20percent%20of%20international%20trade.
