#include <iostream>
#include <string>
using namespace std;

int main()
{
    cout<<"This is a substitution cipher using alphamuneric, \n"<<"punctutations and other items on a regular computer keyboard."<<endl;
    cout<<"Enter your message: "<<endl;
    string plaintext;
    getline(cin,plaintext);
    string sample="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv wxyz`1234567890~!@#$<>?:;'&*'(')-=_+{}[]|";
    string key="DE$<KLF890~!@#de=_+{}bc3467>?ijuvwf'&*'ghMYZGHIJaxyz`12NOP QRSTUVWX:;('klm5nqoprst)-[]|ABC";
    for (int i=0;i<plaintext.length();i++){
        int position=sample.find(plaintext[i]);
        plaintext[i]=key[position];
    }
    string ciphertext=plaintext;
    cout<<"Encryting Message...."<<endl;
    cout<<"Ciphertext: "<<ciphertext<<endl;
    
    cout<<"Decryting Message"<<endl;
    for(int j=0;j<ciphertext.length();j++){
        int new_position=key.find(ciphertext[j]);
        ciphertext[j]=sample[new_position];
    }
    
    string decrypted_message=ciphertext;
    cout<<"The decrypted message is: "<<decrypted_message<<endl;
    
    return 0;
}
