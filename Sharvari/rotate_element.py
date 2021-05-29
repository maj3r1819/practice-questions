{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red109\green109\blue109;\red32\green32\blue32;\red153\green168\blue186;
\red86\green132\blue173;\red191\green100\blue38;\red117\green114\blue185;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c42745\c42745;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c60000\c65882\c72941;
\csgenericrgb\c33725\c51765\c67843;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c45882\c44706\c72549;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 #To rotate one element of the array to the left.\
#IP= [1,2,3,4,5,6,7], k=3\
#OP=[4,5,6,7,1,2,3]\
\cf4 x=[\cf5 1\cf6 ,\cf5 2\cf6 ,\cf5 3\cf6 ,\cf5 4\cf6 ,\cf5 5\cf6 ,\cf5 6\cf6 ,\cf5 7\cf4 ]\
\
n=\cf7 len\cf4 (x);\
temp=x[\cf5 0\cf4 ]; \cf2 #assign a temp variable for the first element\
\cf6 for \cf4 i \cf6 in \cf7 range\cf4 (\cf5 0\cf6 ,\cf4 n-\cf5 1\cf4 ): \cf2 #push the elements to the left to fill the empty first spot\
    \cf4 x[i]=x[i+\cf5 1\cf4 ];\
\
x[n-\cf5 1\cf4 ]=temp;\
\
\cf7 print\cf4 (x)\
\
}