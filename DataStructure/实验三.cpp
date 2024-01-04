#include <iostream>
#include <vector>

using namespace std;

// ������Ԫ���ṹ��
struct Triplet {
    int row;
    int col;
    int value;
};

// ��������
//void createM(vector<Triplet>& M) {
//    int rows, cols, count;
//    cout << "���������������������ͷ���Ԫ�ظ�����";
//    cin >> rows >> cols >> count;
//    
//    Triplet tmp;
//	tmp.row=rows;tmp.col=cols;tmp.value=count;
//    M.push_back(tmp);
//    // �������Ԫ�ص��кš��кź�ֵ
//    for (int i = 0; i < count; i++) {
//        Triplet element;
//        cout << "�������" << i+1 << "������Ԫ�ص��кš��кź�ֵ��";
//        cin >> element.row >> element.col >> element.value;
//        M.push_back(element);
//    }
//}
// ��������
const int N=110;
int vis[N][N];
void createM(vector<Triplet>& M) {
    int rows, cols, count;
    cout << "���������������������ͷ���Ԫ�ظ�����"<<endl;
    cin >> rows >> cols >> count;
        

    if(count > rows*cols)
    {
        cout<<"������󣬷���Ԫ�ظ���ҪС�ڵ������������������������"<<endl;
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
    // �������Ԫ�ص��кš��кź�ֵ
    for (int i = 0; i < count; i++) {
        Triplet element;
        cout << "�������" << i+1 << "������Ԫ�ص��кš��кź�ֵ��"<<endl;
        cin >> element.row >> element.col >> element.value;
        // element.row--; element.col--;
        if(vis[element.row][element.col]==0)
        {
        	M.push_back(element);
        	vis[element.row][element.col]=1;
		}
        else
        {
            cout<<"�������������±��ظ������������룡"<<endl;
            i--;
        }
    }
}
// ��ʾ����
void displayM(const vector<Triplet>& M) {
    int rows = M[0].row;
    int cols = M[0].col;
    
    // ������ά���飬��ʼ��Ϊ��
    int **arr = new int*[rows+1];
    for (int i = 0; i <=rows; i++) {
        arr[i] = new int[cols+1]{0};
    }
    
    // ������Ԫ����䵽��Ӧλ����
    for (int i = 1; i <= M[0].value; i++) {
        int row = M[i].row;
        int col = M[i].col;
        int value = M[i].value;
        arr[row][col] = value;
    }
    
    // �����ά����
    for (int i = 1; i<=rows; i++) {
        for (int j = 1;j<=cols; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    
    // �ͷŶ�ά�����ڴ�
    for (int i = 0; i <=rows; i++) {
        delete[] arr[i];
    }
    delete[] arr;
}

// ת�þ��� - ����һ��ֱ��ת��
vector<Triplet> transposeM(const vector<Triplet>& M) {
    vector<Triplet> T(M.size());
    // T.push_back(M[0]);
    // �������������ͷ���Ԫ�ظ�������
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

// ת�þ��� - ������������ת��
vector<Triplet> fastTransposeM(const vector<Triplet>& M) {
    vector<Triplet> T(M.size());
    
    // ����ת�þ���������������ͷ���Ԫ�ظ���
    T[0].row = M[0].col;//T.mu=M.nu
    T[0].col = M[0].row;//T.nu=T.mu;
    T[0].value = M[0].value;//T.tu=M.tu;
    
    // ���������������ڼ�¼ԭ����ÿ�з���Ԫ�ظ���
    int numCols = M[0].col;
    int *numTerms = new int[numCols]{0};
    
    // ͳ��ÿ�з���Ԫ�ظ���
    for (int i = 1; i <= M[0].value; i++) {
        int col = M[i].col;
        numTerms[col]++;
    }
    
    // �����������飬��¼ת�ú�ÿ����ת�þ����е���ʼλ��
    int *startPos = new int[numCols]{0};
    
    // ����ÿ����ʼλ��
    for (int i = 2; i <= numCols; i++) {
        startPos[i] = startPos[i - 1] + numTerms[i - 1];
    }
    
    // ������Ԫ��ת��
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
        cout << "��ѡ�������" << endl;
        cout << "1. ��������" << endl;
        cout << "2. ���پ���" << endl;
        cout << "3. �������" << endl;
        cout << "4. ת�þ���" << endl;
        cout << "5. ����ת�þ���" << endl;
        cout << "0. �˳�" << endl;
        cout << "������ѡ�";
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
                cout << "ֱ��ת�ý����" << endl;
                displayM(T);
                break;
            }
            case 5: {
                vector<Triplet> T = fastTransposeM(M);
                cout << "����ת�ý����" << endl;
                displayM(T);
                break;
            }
            case 0:
                return 0;
            default:
                cout << "��Ч��ѡ�������ѡ��" << endl;
                break;
        }
    }
    
    return 0;
}