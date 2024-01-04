#include <iostream>
#include <vector>

using namespace std;

// 定义三元组表结构体
struct Triplet {
    int row;
    int col;
    int value;
};

// 创建矩阵
//void createM(vector<Triplet>& M) {
//    int rows, cols, count;
//    cout << "请输入矩阵的行数、列数和非零元素个数：";
//    cin >> rows >> cols >> count;
//    
//    Triplet tmp;
//	tmp.row=rows;tmp.col=cols;tmp.value=count;
//    M.push_back(tmp);
//    // 输入非零元素的行号、列号和值
//    for (int i = 0; i < count; i++) {
//        Triplet element;
//        cout << "请输入第" << i+1 << "个非零元素的行号、列号和值：";
//        cin >> element.row >> element.col >> element.value;
//        M.push_back(element);
//    }
//}
// 创建矩阵
const int N=110;
int vis[N][N];
void createM(vector<Triplet>& M) {
    int rows, cols, count;
    cout << "请输入矩阵的行数、列数和非零元素个数："<<endl;
    cin >> rows >> cols >> count;
        

    if(count > rows*cols)
    {
        cout<<"输入错误，非零元素个数要小于等于行数乘列数，请从新输入"<<endl;
        return ;
    }
    Triplet tmp;
	tmp.row=rows;tmp.col=cols;tmp.value=count;
    M.push_back(tmp);
    for(int i=0;i<=rows;i++)
    {
    	for(int j=0;j<=cols;j++)
    	{
    		vis[i][j]=0;
		}
	}
    // 输入非零元素的行号、列号和值
    for (int i = 0; i < count; i++) {
        Triplet element;
        cout << "请输入第" << i+1 << "个非零元素的行号、列号和值："<<endl;
        cin >> element.row >> element.col >> element.value;
        // element.row--; element.col--;
        if(vis[element.row][element.col]==0)
        {
        	M.push_back(element);
        	vis[element.row][element.col]=1;
		}
        else
        {
            cout<<"输入错误，输入的下标重复，请重新输入！"<<endl;
            i--;
        }
    }
}
// 显示矩阵
void displayM(const vector<Triplet>& M) {
    int rows = M[0].row;
    int cols = M[0].col;
    
    // 创建二维数组，初始化为零
    int **arr = new int*[rows+1];
    for (int i = 0; i <=rows; i++) {
        arr[i] = new int[cols+1]{0};
    }
    
    // 将非零元素填充到对应位置上
    for (int i = 1; i <= M[0].value; i++) {
        int row = M[i].row;
        int col = M[i].col;
        int value = M[i].value;
        arr[row][col] = value;
    }
    
    // 输出二维数组
    for (int i = 1; i<=rows; i++) {
        for (int j = 1;j<=cols; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    
    // 释放二维数组内存
    for (int i = 0; i <=rows; i++) {
        delete[] arr[i];
    }
    delete[] arr;
}

// 转置矩阵 - 方法一：直接转置
vector<Triplet> transposeM(const vector<Triplet>& M) {
    vector<Triplet> T(M.size());
    // T.push_back(M[0]);
    // 将行数、列数和非零元素个数调换
    T[0].row = M[0].col;
    T[0].col = M[0].row;
    T[0].value = M[0].value;
    int q=1;
    for(int col=1;col<=M[0].col;col++)
    {
    	for(int p=1;p<=M[0].value;p++)
    	{
    		if(M[p].col==col)
    		{
    			T[q].col=M[p].row;
    			T[q].row=M[p].col;
    			T[q].value=M[p].value;
    			q++;
    		}
    	}
    }

    return T;
}

// 转置矩阵 - 方法二：快速转置
vector<Triplet> fastTransposeM(const vector<Triplet>& M) {
    vector<Triplet> T(M.size());
    
    // 设置转置矩阵的行数、列数和非零元素个数
    T[0].row = M[0].col;//T.mu=M.nu
    T[0].col = M[0].row;//T.nu=T.mu;
    T[0].value = M[0].value;//T.tu=M.tu;
    
    // 建立辅助数组用于记录原矩阵每列非零元素个数
    int numCols = M[0].col;
    int *numTerms = new int[numCols]{0};
    
    // 统计每列非零元素个数
    for (int i = 1; i <= M[0].value; i++) {
        int col = M[i].col;
        numTerms[col]++;
    }
    
    // 建立辅助数组，记录转置后每列在转置矩阵中的起始位置
    int *startPos = new int[numCols]{0};
    
    // 计算每列起始位置
    for (int i = 2; i <= numCols; i++) {
        startPos[i] = startPos[i - 1] + numTerms[i - 1];
    }
    
    // 将非零元素转置
    for (int i = 1; i <= M[0].value; i++) {
        int col = M[i].col;
        int j = startPos[col];
        T[j].row = M[i].col;
        T[j].col = M[i].row;
        T[j].value = M[i].value;
        startPos[col]++;
    }
    
    delete[] numTerms;
    delete[] startPos;
    
    return T;
}

int main() {
    vector<Triplet> M;
    
    while (true) {
        int option;
        cout << "请选择操作：" << endl;
        cout << "1. 创建矩阵" << endl;
        cout << "2. 销毁矩阵" << endl;
        cout << "3. 输出矩阵" << endl;
        cout << "4. 转置矩阵" << endl;
        cout << "5. 快速转置矩阵" << endl;
        cout << "0. 退出" << endl;
        cout << "请输入选项：";
        cin >> option;
        
        switch (option) {
            case 1:
                createM(M);
                break;
            case 2:
                M.clear();
                break;
            case 3:
                displayM(M);
                break;
            case 4: {
                vector<Triplet> T = transposeM(M);
                cout << "直接转置结果：" << endl;
                displayM(T);
                break;
            }
            case 5: {
                vector<Triplet> T = fastTransposeM(M);
                cout << "快速转置结果：" << endl;
                displayM(T);
                break;
            }
            case 0:
                return 0;
            default:
                cout << "无效的选项，请重新选择！" << endl;
                break;
        }
    }
    
    return 0;
}