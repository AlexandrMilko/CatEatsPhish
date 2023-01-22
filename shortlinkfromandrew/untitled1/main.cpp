#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include <cstdlib>
using namespace std;
int main() {
    string str;
    cin>>str;
    system(("python3 download_html_file.py " + str).c_str());
    string html;
    ifstream input("downloaded_html.html");
    if(input) {
        ostringstream ss;
        ss << input.rdbuf();
        html = ss.str();
    }
    string bitly="bit.ly/", cuttly="cutt.ly/", tly="t.ly/", tinyurlcom="tinyurl.com/", rotflol="rotf.lol/", tinyone="tiny.one/", shorturlat="shorturl.at/";
    int flag=0;
    if(html.find(bitly)!= string::npos)
    {
        flag=1;
    }
    if(html.find(cuttly)!= string::npos)
    {
        flag=1;
    }
    if(html.find(tly)!= string::npos)
    {
        flag=1;
    }
    if(html.find(tinyurlcom)!= string::npos)
    {
        flag=1;
    }
    if(html.find(rotflol)!= string::npos)
    {
        flag=1;
    }
    if(html.find(tinyone)!= string::npos)
    {
        flag=1;
    }
    if(html.find(shorturlat)!= string::npos)
    {
        flag=1;
    }
    cout<<flag;
    return 0;
}