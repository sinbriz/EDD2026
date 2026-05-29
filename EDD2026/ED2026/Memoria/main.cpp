#include <iostream>
using namespace std;
int ga;
int gb[10];
int gn = 20;
int gc[20];

class Emp {
public:
int id;
string emp_name;
int *day;
// Constructor to initialize employee details
Emp(int id, string emp_name) {
this->id = id;
this->emp_name = emp_name;
this->day = new int[10];
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&id)) << "," << &id
<< ",id_c" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&emp_name)) <<
"," << &emp_name << ",emp_name_c" << endl;

cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(day)) << "," <<
&day << ",this->day_c" << endl;
}
Emp(const Emp &perc_) {
this->id = perc_.id;
this->emp_name = perc_.emp_name;
this->day = new int[10];
for (int i = 0; i < 10; i++)
this->day[i] = perc_.day[i];
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&perc_)) << ","
<< &perc_ << ",perc_cc" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&id)) << "," <<
&id << ",this->id_cc" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&emp_name))
<< "," << &emp_name << ",this->emp_name_cc" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(day)) << "," <<
&day << ",this->day_cc" << endl;
}
~Emp()
{
delete [] day;
}
};
// Function to create and return an Emp object
Emp Emp_detail(int id, string emp_name) {
Emp per_f(id, emp_name);
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&id)) << "," << &id
<< ",id_f" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&emp_name)) <<
"," << &emp_name << ",emp_name_f" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&per_f)) << "," <<
&per_f << ",per_f" << endl;
return per_f;
}
int main()
{
// Todas estas variables obtienen memoria
// asignada en el stack
int a;

int b[10];
int n = 20;
int c[n];
cout << "DecValue,HexValue,Label" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&ga)) << "," <<
&ga << ",ga" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(gb)) << "," << gb
<< ",gb" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&gn)) << "," <<
&gn << ",gn" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(gc)) << "," << gc
<< ",gc" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&a)) << "," << &a
<< ",a" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(b)) << ","<< b <<
",b" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&n)) << "," << &n
<< ",n" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(c)) << "," << c <<
",c" <<endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>((void *) main)) <<
"," << (void *) main << ",main" << endl;
int *pa = new int;
int *pb = new int[10];
int *pn = new int(20);
int *pc = new int[*pn];
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(pa)) << "," << pa
<< ",pa" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(pb)) << "," << pb
<< ",pb" << endl;
cout <<static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(pn)) << "," << pn <<
",pn" <<endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(pc)) << "," << pc
<< ",pc" <<endl;
// Initializing employee details
int id = 21;
string name = "Maddy";
// Creating an Emp object using the function
Emp person_ = Emp_detail(id, name);
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&id)) << "," << &id
<< ",id" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&name)) << "," <<

&name << ",name" << endl;
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&person_)) << ","
<< &person_ << ",person_" << endl;
Emp*per_2 = new Emp(person_);
cout << static_cast<unsigned long long>(reinterpret_cast<std::uintptr_t>(&per_2)) << "," <<
&per_2 << ",per_2" << endl;
delete pa;
delete [] pb;
delete pn;
delete [] pc;
delete per_2;
return 0;
}
