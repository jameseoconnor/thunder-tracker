## A thunder tracker to warn you about an iminent thunderstorm 
So we have a dog at home, called Alfie, who went missing on us twice during thunderstorms. So I created this simple AWS Lambdafunction to monitor the weather near our house, by polling the accuweather API to see if any thunder has been forecast. An SNS is then sent to out to our family members to tell us to bring him inside. It works surprisingly well! 

<p align="center">
<img src="./images/alfie_1.jpeg" width=40%>
</p>

I am hoping to wrap it inside a product at some stage where users can submit their general location and email address(es) to get notified if a thunderstorm is nearby or forecast. 