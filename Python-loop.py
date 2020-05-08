Divisible by Ten

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i%10 == 0:
      count += 1
  return count


#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

Greetings

#Write your function here
def add_greetings(names):
  lst = []
  for i in range(len(names)):
    lst.append("Hello, " + names[i])
  return lst


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

Delete Starting Even Numbers

#Write your function here
def delete_starting_evens(lst):
  
  for index in range(len(lst)):
    if lst[0] %2 == 0:
      lst.pop(0)
  return lst
      
      
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

Odd Indices

#Write your function here
def odd_indices(lst):
  lst1=[]
  for i in range(len(lst)):
    if i%2 !=0:
      lst1.append(lst[i])
  return lst1 

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

Exponents

#Write your function here
def exponents(bases,powers):
  lst=[]
  for i in range(len(bases)):
    for j in range(len(powers)):
      lst.append(bases[i]**powers[j])
  return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

Larger Sum

#Write your function here
def larger_sum(lst1,lst2):
  tot1=0
  tot2=0
  for i in range(len(lst1)):
    tot1 = tot1 + lst1[i]
  for j in range(len(lst2)):
    tot2 = tot2 + lst2[j]
  if tot1 > tot2:
    return lst1
  elif tot2 > tot1:
    return lst2
  else:
    return lst1  



#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

Over 9000
 
#Write your function here
def over_nine_thousand(lst):
  tot = 0
  for i in range(len(lst)):
    tot = tot + lst[i]
    if tot > 9000:
      break
  return tot
  if tot < 9000:
    return tot
    if lst == []:
      return 0    


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

Max Num
 
#Write your function here
def max_num(nums):
  for num in nums:
    return max(nums)
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

Same Values

#Write your function here
def same_values(lst1,lst2):
  lst_idx=[]
  if len(lst1) == len(lst2):
    for i in range(len(lst1)):
      if lst1[i] == lst2[i]:
        lst_idx.append(i)
  return lst_idx


#Uncomment the line below when your function is done
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

Reversed List

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))
