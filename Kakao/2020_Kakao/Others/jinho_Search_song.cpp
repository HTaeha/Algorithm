#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string>
using namespace std;
const int ALPHABET_SIZE = 'z' - 'a' + 1;
struct Node
{
    Node *children[ALPHABET_SIZE];
    bool isEndofword;

    unordered_map<int, int> M;
};

struct Node *getNode(void)
{
    Node *newNode = new Node;

    newNode->isEndofword = false;

    for (int i = 0; i < ALPHABET_SIZE; ++i)
    {
        newNode->children[i] = nullptr;
    }
    newNode->M.clear();

    return newNode;
}

void insert(struct Node *root, string str)
{
    struct Node *currentNode = root;

    for (int i = 0; i < str.size(); ++i)
    {
        int index = str[i] - 'a';
        currentNode->M[str.size() - i]++;
        if (currentNode->children[index] == nullptr)
        {
            currentNode->children[index] = getNode();
        }
        currentNode = currentNode->children[index];
    }
    currentNode->M[0]++;
    currentNode->isEndofword = true;
}

void displayAll(vector<string> &returnV, struct Node* root, string str)
{   
    if (root->isEndofword)
    {
        returnV.push_back(str);
    }

    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (root->children[i])
        {
            displayAll(returnV, root->children[i], str + string(1, char(i + 'a')));
        }
    }
}

int cnt;
void search(struct Node *root, string str)
{
    struct Node *currentNode = root;

    for (int i = 0; i < str.size(); ++i)
    {
        if (str[i] == '?')
        {
            cnt = currentNode->M[str.size() - i];
            return;
        }
        else
        {
            int idx = str[i] - 'a';
            if (currentNode->children[idx] == nullptr)
            {
                return;
            }
            currentNode = currentNode->children[idx];
        }
    }
}

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;

    struct Node *root = getNode();
    struct Node *reverseRoot = getNode();
    for (int i = 0; i < words.size(); ++i)
    {
        insert(root, words[i]);
        reverse(words[i].begin(), words[i].end());
        insert(reverseRoot, words[i]);
    }
    for (int i = 0; i < queries.size(); ++i)
    {
        cnt = 0;
        if(queries[i][0] != '?')
            search(root, queries[i]);
        else
        {
            reverse(queries[i].begin(), queries[i].end());
            search(reverseRoot, queries[i]);
        }
        answer.push_back(cnt);
    }
    return answer;
}
