#Write a program that reads a number from the standard input, then draws a
#square like this:
'''
%%%%%
%%  %
% % %
%  %%
%   %
%%%%%
'''
#The square should have as many lines as the number was
num = int(input("Please enter an integer number: "))
percent = "%"
space = " "
for i in range(0, num):
    if i == 0 or i == num - 1:
        print(percent * num)
    elif i in range(1, num - 1):
        print(percent + space * (i - 1) + percent + space * (num - i - 2) + percent)