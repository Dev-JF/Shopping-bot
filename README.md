# Shopping-bot
This bot is so you can beat the scalpers and use a bot to buy items that are usually scalped

before you get started:


about the shopbot:

The shopbot first connects to a proxy to help prevent being blocked

Then the shopbot checks the Store_Info.json file to see what stores are being checked

The shopbot then checks if the link is available and gets the status code of the website

If the site is available then the application loads the stores json file and loops through each json line





First in the Store_Info json file add the store name, the url of the product you  want to watch

Then create a json file with the same store name e.g. Kmart.json

In that store json file:

add the steps you would go through on the website in the stores json file, label the button and put the link in the jon file

e.g. "addToCart":{"button":"/html/body/div[11]/section[1]/div[7]/div/div[1]/div[1]/a", "value":"bttn1" }

For example the steps are: add the item to the cart, go to the cart, checkout, input purchase information, etc.

Note: there is an example Kmart.json file.












Things that need to be added

User interface



