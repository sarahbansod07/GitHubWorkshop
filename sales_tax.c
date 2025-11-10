#include<stdio.h>
int main()
{

int printed_price,discount_percentage,tax_percentage,Discounted_Price,After_Tax;

printf("Enter Printed Price: ");
scanf("%d, &printed_price");

printf("Enter Discount Percentage: ");
scanf("%d, &discount_percentage");

printf("Enter Sales Tax: ");
scanf("%d, &tax_percentage");

Discounted_Price = printed_price - ((printed_price *discount_percentage)/100);
printf("Discounted Price: ", Discounted_Price);

After_Tax = Discounted_Price + ((Discounted_Price*tax_percentage)/100);
print("Final Price: ",After_Tax);

return 0; 
}