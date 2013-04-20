// simple date class
// wfp, 10/24/07
// rje, converted to C++, 12/3/07

#include <iostream>
#include <string>
using namespace std;

bool validDate(int day,int month,int year)
{
    //very gross check of the size of day, month and year 
    if ((1<= day)&& (day <=31) && (1<= month) && (month <=12) &&  (0<= year))
        return true;
    else
        return false;
}
class Date
{
  public:
    Date(int d = 1, int m = 1, int y = 2000);
    void printDate(ostream&) const;
    void strUpdate(string dateStr);
    
  private:
    int day;
    int month;
    int year;
    string monthArray[12];
};  // watch out for this semicolon!!

Date::Date(int d, int m, int y)
{
  string mArray[12]={"January","February","March","April","May","June", "July","August","September","October","November","December"};
  day = d;
  month = m;
  year = y;
  for (int i = 0; i < 12; i++)
    monthArray[i] = mArray[i];
}

void Date::printDate(ostream& Out) const
{
  Out << monthArray[month-1] << " " << day << ", " << year << endl;
}

void Date::strUpdate(string dateStr) 
{
   int pos1, pos2;  // positions of slashes
   string dayStr, monthStr, yearStr; // day, month, and year as stings
   int dayInt, monthInt, yearInt;
   pos1 = dateStr.find('/');  // find first slash
   pos2 = dateStr.find('/', pos1+1); // find next slash (start searching a pos1+1)
   dayStr = dateStr.substr(0,pos1);  // copy pos1 number of characters starting at position 0
   monthStr = dateStr.substr(pos1+1, pos2-pos1-1);
   yearStr = dateStr.substr(pos2+1);
   //cout << dayStr << "/" << monthStr << "/" << yearStr << endl;
   dayInt = atoi(dayStr.c_str());
   monthInt = atoi(monthStr.c_str());
   yearInt = atoi(yearStr.c_str());
   if (validDate(dayInt,monthInt,yearInt))
   {
       day = dayInt;
       month = monthInt;
       year = yearInt;
   }
   else
       cout << "invalid date, date not changed";
}

ostream& operator<<( ostream& Out, const Date& Item )
{
  Item.printDate( Out );
  return Out;
}

int main()
{
  Date D(3,4,2005);
  //D.printDate(cout);
  cout << D ;
  D.strUpdate("5/12/2006");
  //D.printDate(cout);
  cout << D ;
}
