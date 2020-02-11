#include <stdio.h>
typedef char BData;
typedef struct _bTreeNode{
    BData item;
    struct _bTreeNode * left;
    struct _bTreeNode * right;
} BTreeNode;
BTreeNode * CreateNode(BData item){
    BTreeNode * node = (BTreeNode*)malloc(sizeof(BTreeNode));
    node->item = item;
    node->left = NULL;
    node->right = NULL;
}
void CreateLeftSubtree(BTreeNode* root, BTreeNode * left)
{
    if (root->left != NULL)
        exit(1);

    root->left = left;
}
void CreateRightSubtree(BTreeNode* root, BTreeNode * right)
{
    if (root->right != NULL)
        exit(1);

    root->right = right;
}
BTreeNode* BuildTree(BData* arr, int n)
{
    int i;
    BTreeNode* root;
    BTreeNode ** tree = (BTreeNode **)malloc(sizeof(BTreeNode*)* n);

    for (i = 0; i < n; i++) {
        if (arr[i] == '.')    // Avoid generating a node.
            continue;
        if (i == 0)
            tree[0] = CreateNode(arr[i]);
        else if (i % 2 == 0) {
            tree[i] = CreateNode(arr[i]);
            CreateRightSubtree(tree[(i - 1) / 2], tree[i]);
        }
        else {
            tree[i] = CreateNode(arr[i]);
            CreateLeftSubtree(tree[(i - 1) / 2], tree[i]);
        }
    }
    root = tree[0];
    free(tree);
    return root;
}
int main(){
    int n;
    char arr[3];
    scanf("%d",&n);

    while(n--){
        scanf("%c %c %c",&arr[0],&arr[1],&arr[2]);

    }
}
