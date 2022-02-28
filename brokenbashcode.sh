#!/usr/bin/bash

!echo -e "What is your name?:  "
read name
echo -e "How old are you?: "
read age
echo -e "Where are you from?: "
read origin
echo -e "What is your favorite color?: "
read color
echo -e "What is your favorite activity?: "
read hobby
#Each variable in this line had an "s" after it, I went through and removed the s's so that the program would detect the variables and display the required info!
echo "It's so cool that your name is $name and that you're $age years old. $origin sounds like a neat place to grow up! My favorite color is $color too! Maybe we could try $hobby together sometime!"
