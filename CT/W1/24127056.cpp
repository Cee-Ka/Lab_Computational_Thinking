#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <ctime>
using namespace std;

class Question {
private:
    string text;
    int index;
public:
    Question(const string &_text, int _index) : text(_text), index(_index) {}

    static string ask(const vector<Question> &_questions) {
        string localPart = "";
        for (const auto &q : _questions) {
            cout << q.text;
            string ans;
            getline(cin, ans);
            ans.erase(remove(ans.begin(), ans.end(), ' '), ans.end());
            if (ans.length() >= q.index)
                localPart += tolower(ans[q.index - 1]);
            else
                localPart += char('a' + rand() % 26);
        } 
        return localPart;
    }
};

string encode(const string &text, int shift) {
    string result = text;
    for (char &ch : result) {
        if (isalpha(ch)) {
            char base = islower(ch) ? 'a' : 'A';
            ch = (ch - base + shift + 26) % 26 + base;
        }
    }
    return result;
}

int main() {
    srand(time(0));
    string destination_1 = "fof.ilwxv.hgx.yq";
    string destination_2 = "kdqk";
    string code = to_string(1202 * 2 + 4);
    encode(destination_1, 5);
    encode(destination_2, 5);

    cout << "Welcome to my quiz!\n";
    cout << "Please answer all the questions by using only one word in English\n";
    vector<Question> questions = {
        Question("In programming, what memory area is used for dynamic allocation during runtime? ", 4),
        Question("What is the capital of Australia? ", 1),
        Question("What key can not open any door? " , 4)
    };
    string part = Question::ask(questions);
    
    cout << "WELL DONE!";
    cout << "\nPlease send invitation via: " << part + encode(destination_2, -3) + code + '@' + encode(destination_1, -3) << "\n";
    return 0;
}
