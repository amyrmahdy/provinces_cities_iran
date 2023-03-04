# Case
The case is to scrap wikipedia to achive Iran's provinces and cities in json format. 
There is [List of cities in Iran by province in english](https://wikipedia.lurkmore.com/wiki/List_of_cities_in_Iran_by_province?lang=en) which scraped, **but** the problem was with [List of cities in Iran by province in persian](https://wikipedia.lurkmore.com/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86?lang=fa), because tables in mentioned link were super confusing! So, used [List of cities in Iran by province in english translated to persian](https://wikipedia-lurkmore-com.translate.goog/wiki/List_of_cities_in_Iran_by_province?lang=en&_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=fa) but without requests library or selenium library, because both of their response was without persian text, thus downloaded the html to solve the problem, **but** three city names couldnt be translated and they had been handled manualy:

1 - [Mohr](https://wikipedia-lurkmore-com.translate.goog/wiki/Mohr,_Fars?lang=en&_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=fa)

2 - [Senderk](https://wikipedia-lurkmore-com.translate.goog/wiki/Senderk?lang=en&_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=fa)

3 - [Hojedk](https://wikipedia-lurkmore-com.translate.goog/wiki/Hojedk?lang=en&_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=fa
)

ps: There was older version using googletrans library that was not accurate enough. 


Author: amyrmahdy

Date: 3 March 2023

