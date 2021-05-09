# IOT-BASED-DEVICE-CONTROLLING-SYSTEM-WITH-GUI-USING-PYTHON-NODEMCU-AND-THINGSPEAK
In this project I have shown how we can control our machines from anywhere in the world using Internet of Things.
So for this I have made a Graphical User Interface using python which use to take input from the user like which colour of the light you want to turn on, for how much time you want a light or dc brushed motor or a servo motor to run , if you want to turn the servo motor in clockwise or anticlockwise direction, for how much degree you want to rotate the servo motor etc. 
Once a user will enter the required values according to the task he/she you needs to perform, our python program will send the required values to perform the task to the thingspeak server. 
Now our nodemcu program will come into role. Now our NodeMcu will fetch all the data from the ThingSpeak server and then will check in the program that which task it has to perform now. Once it will get to know the task it has to perform then that task will be executed.
In my Graphical User Interface a user can specify following types of details:-
                   1) Light colour
                   2) For how much time a light hould be switched on.
                   3) Motor rotation type(clockwise or anticlockwise).
                   4) For how much time the motor should be turned on.
                   5) To how much angle a servo needs to be rotated.
                   6) For how many times our servo motor should perform the same task.
Please note that if you want the light, or motor or servo to work continously without any break then apply the following values in GUI :-
                   1) Run time = 0
                   2) Number of time = 0
This project is just to show you that how now a days in Industy 4.0 revolution they are using IOT to control machines from anywhere.
Following are the benefits of using IOT to control machines :- 
                   1) Labour cost is redused.
                   2) A user can maintain or make changes in the machine from anywhere in the world, just you need is a good wifi connection with the machine and with the user                           which now a days all of have. It does not matter weather a user is relaxing in his/her home our working very far from the machine. 
                   3) We can also use this system to analyse the problem which a machine is facing during the task. You will have all the data on you pc.
                   4) You can easily make changes in the sensor values, motor rotation speed(rpm) etc and make that machine flexible to do multiple task. You dont need to make a                         new machine for a different task, you can make many products from a single machine withour touching it physically and without going to the Industry where a                         task needs to be performed.
                   5) This system will also help in saving money, material, resources, labour cost etc.
******************************************************************************************************************************************************************************
If you want to learn more about these type of projects the do visit my YouTube channel :- 
YouTube channel link :-  https://youtube.com/channel/UCsKfPerC5SseOFjiZ5Zy7Xg 
You will find all the other details about this project on my YouTube channel!!
