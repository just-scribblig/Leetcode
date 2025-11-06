class Solution {
public:
    bool isValid(string s) {
        stack<char> a;
        for (char ch: s){
            if (ch=='{' || ch=='[' || ch=='(')
                a.push(ch);
            else{
                if (a.empty()) return false;
                else{
                    char top=a.top();
                    a.pop();
                    if (ch==']' && top!='[') return false;
                    if (ch=='}' && top!='{') return false;
                    if (ch==')' && top!='(') return false;
                }
            }
        }
        return a.empty();
    }
};