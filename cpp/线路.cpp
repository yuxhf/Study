#include<stdlib.h>  //����system��ϵͳ����
#include<stdio.h>
#include<conio.h>  //������ͨ�������̲����Ķ�Ӧ����
#include<string.h>  //��ʹ�õ��ַ�����ʱ��Ҫʹ��
#define Infinity      32767       //ͼ�ľ�����A��i��i����Ϊ0����û��ͨ·����ΪINFINITY = 32762 
#define MAXV    100  //��󾰵�����Ϊ40
#define INF 32767


typedef struct{
	int num;//����ı�� 
	char name[30];//�������� 
	char info[100];//�����������Ϣ 
}VertexType;//��������� 

typedef struct{
	int edges[MAXV][MAXV];//�ڽӾ������� 
	int n,e;//������������ 
	VertexType vexs[MAXV];//��Ŷ������Ϣ 
}MGraph; //������ͼ�ڽӾ������� 


MGraph g;
void map();
void Search(MGraph g);
void deal();
void Floyd(MGraph g);
void Dispath(MGraph g,int A[][MAXV],int path[][MAXV]);
void Dispath1(MGraph g,int dist[],int path[],int S[],int v);



 



 MGraph InitGraph()  //��ʼ������ͼ  
{
	int i=0,j=0;
	g.n=7;//����ͼ������� 
	g.e=12;//���� 
	for(i=0;i<g.n;i++)
		g.vexs[i].num=i;
	strcpy(g.vexs[0].name,"��ѧ¥");
	strcpy(g.vexs[0].info,"��������ѧԺ�ر꽨��,Ҳ����ߵĽ���");
	strcpy(g.vexs[1].name,"ͼ���");
	strcpy(g.vexs[1].info,"�����������,��ʩ����,��������,�ʺ�Ǳ�Ķ���");
	strcpy(g.vexs[2].name,"��"); 
	strcpy(g.vexs[2].info,"�˶���ֹ��,������к��Ӷ�˧");
	strcpy(g.vexs[3].name,"�ٳ�");
	strcpy(g.vexs[3].info,"������ʺ�ɢ�� ����,�㶮��");
	strcpy(g.vexs[4].name,"��Ԣ(��)");
	strcpy(g.vexs[4].info,"�к��ӵ�����");
	strcpy(g.vexs[5].name,"��Ԣ(Ů)");
	strcpy(g.vexs[5].info,"Ů���ӵ�����");
	strcpy(g.vexs[6].name,"����");
	strcpy(g.vexs[6].info,"�Է��ĵط�����˵");

	for(int i=0;i<g.n;i++)
	  for(int j=0;j<g.n;j++)
			g.edges[i][j]=Infinity;
			g.edges[0][1]=g.edges[1][0]=200;
			g.edges[0][6]=g.edges[6][0]=175;
			g.edges[0][5]=g.edges[5][0]=275;
			g.edges[1][2]=g.edges[2][1]=200;
			g.edges[2][3]=g.edges[3][2]=225;
			g.edges[3][4]=g.edges[4][3]=275;
			g.edges[4][5]=g.edges[5][4]=250;
		    g.edges[5][6]=g.edges[6][5]=200;
			g.edges[1][6]=g.edges[6][1]=175;
			g.edges[2][6]=g.edges[6][2]=250;
			g.edges[3][6]=g.edges[6][3]=375;
			g.edges[4][6]=g.edges[6][4]=300;
																						 												 									                                        
		return g;
}




void map()//ѧУƽ��ͼ 
{
	printf("\t*******************�Ѽ���У԰��ƽ��ͼ!*********************\t\n");
    printf("\t...........................................................\t\n");
	printf("\t.             ...........                                 .\t\n");
	printf("\t.             . 1.      .  ..............       .......   .\t\n");
	printf("\t.  ........   .  ͼ��� .  .2.  ��    .       .3.   .   .\t\n");
	printf("\t.  . 0.   .   ...........  ..............       .     .   .\t\n");
	printf("\t.  .  ��  .                                     .  �� .   .\t\n");
	printf("\t.  .  ѧ  .                                     .     .   .\t\n");
	printf("\t.  .  ¥  .    ..........                       .     .   .\t\n");
	printf("\t.  .      .    . 6.���� .                       .  �� .   .\t\n");
	printf("\t.  ........    ..........                       .     .   .\t\n");
	printf("\t                                                .......   .\t\n");
	printf("\t.           .............     .............               .\t\n");
	printf("\t.           . 5. ��Ů   .     . 4.���У�  .               .\t\n");
    printf("\t.           .    ��Ԣ   .     .    ��Ԣ   .               .\t\n");
	printf("\t.           .............     .............               .\t\n");
	printf("\t...........................................................\t\n");	


}


void Search(MGraph g)
{	
	int i;
	printf("���\t��������\t\t������\t\t\n");
	printf("____________________________________________________________________________\n");
	for(i=0;i<g.n;i++)
	printf("%-10d%-25s%-80s\n",g.vexs[i].num,g.vexs[i].name,g.vexs[i].info);
	printf("____________________________________________________________________________\n");
	printf("\n"); 
	deal();
}



void Dijkstra(MGraph g,int v)//�Ͻ�˹�����㷨 
{   
	int dist[MAXV],path[MAXV];
	int S[MAXV];
	int MINdis,i,j,u;
	for(i=0;i<g.n;i++)
	{
		dist[i]=g.edges[v][i];
		S[i]=0;
		if(g.edges[v][i]<Infinity )
		{
			path[i]=v;
		}
		else
		{
			path[i]=-1;
		}
	}
	S[v]=1;
	path[v]=0;
	for(i=0;i<g.n-1;i++)
	{
		MINdis=Infinity ;
		for(j=0;j<g.n;j++)
		{
			if(S[j]==0 && dist[j]<MINdis)
			{
				u=j;
				MINdis=dist[j];
			}
		}
		S[u]=1;
		for(j=0;j<g.n;j++)
		{
			if(S[j]==0)
			{
				if(g.edges[u][j]<Infinity  && dist[u]+g.edges[u][j]<dist[j])
				{
					dist[j]=dist[u]+g.edges[u][j];
					path[j]=u;
				}
			}
		}
	}
	Dispath1(g,dist,path,S,v);
	printf("\n") ;
	deal();
}



void Dispath1(MGraph g,int dist[],int path[],int S[],int v)
{   
	int i,j,k;
	int apath[MAXV],d;
	for(i=0;i<g.n;i++)
	{
		if(i!=v)
		{
		
		if(S[i]==1 && i!=v)
		{
			printf("%s �� %s �ĳ����� %d �� , ·���� ",g.vexs[v].name,g.vexs[i].name,dist[i]);
		}
		d=0;
		apath[d]=i;
		k=path[i];
		if(k==-1)
		{ 
			printf("��·��\n");
		}
		else
		{
			while(k!=v)
			{
				d++;
				apath[d]=k;
				k=path[k];
			}
			d++;
			apath[d]=v;
			printf("%d--->",apath[d]);
			for(j=d-1;j>=0;j--)
			{
				printf("%d",apath[j]);
					if(j>=1)
				printf("--->");
			}
			printf("\n");
		}
	}
	else{
         	printf("");
		 }
}
         
}



void Floyd(MGraph g)//Floyd�㷨 
{
    int flag=0;
	int A[MAXV][MAXV],path[MAXV][MAXV];
	int i,j,k;
	for(i=0;i<g.n;i++)
		for(j=0;j<g.n;j++)
		{
			A[i][j]=g.edges[i][j];
			if(i!=j && g.edges[i][j]<INF)
				path[i][j]=i;
			else
				path[i][j]=-1;
		}
		for(k=0;k<g.n;k++)
		{
			for(i=0;i<g.n;i++)
				for(j=0;j<g.n;j++)
					if(A[i][j]>A[i][k]+A[k][j])
					{
						A[i][j]=A[i][k]+A[k][j];
						path[i][j]=path[k][j];
					}
		}
		Dispath(g,A,path);//������·��
		printf("\n");
		deal();
}



void Dispath(MGraph g,int A[][MAXV],int path[][MAXV])
{	
    int flag=0;
	int i,j,k,s,q,t;
	printf("���������������: ");
    do
		{   	
		   if(!scanf("%d",&q))	
		      {	
		      scanf("%*[^\n]");
		      flag=0;
	          }
	       	else if(!(q==0||q==1||q==2||q==3||q==4||q==5||q==6))
	        	{
	        		 scanf("%*[^\n]");
	        		 flag=0;
				} 
				else
				{
					scanf("%*[^\n]");
					flag=1;break;
				}
				scanf("%*[^\n]");
				printf("���������������:");
				fflush(stdin);
		}while(flag==0);
		

	printf("����������Ŀ�ĵأ�");
   do
		{	
		    if(!scanf("%d",&t))	
		      {	
		        scanf("%*[^\n]");
		        //scanf("%*c");
		        flag=0;
	          }
	      else 	if(!(t==0||t==1||t==2||t==3||t==4||t==5||t==6))
	        	{
	        		scanf("%*[^\n]");
		            //scanf("%*c");
	        		flag=0;
				} 
				else
				{
			     	scanf("%*[^\n]");
		            //scanf("%*c");
					flag=1;break;
				}
				scanf("%*[^\n]");
		        //scanf("%*c");
			    printf("���棡��������������Ŀ�ĵأ�");
				fflush(stdin);
		}while(flag==0);	
    printf("\n");
	int apath[MAXV],d;
	for(i=0;i<g.n;i++)
		for(j=0;j<g.n;j++)	
		{
	
			if(A[i][j]!=INF && i!=j)
			{
			    if(i==q&&j==t)
			    {
				
				printf("%s  ��  %s ��·���� ",g.vexs[i].name,g.vexs[j].name);
				k=path[i][j];
				d=0;apath[d]=j;
				while(k!=-1 && k!=i)
				{
					d++;apath[d]=k;
					k=path[i][k];
				}
				d++;apath[d]=i;
				printf("%d--->",apath[d]);
				for(s=d-1;s>=0;s--)
				{
				printf("%d",apath[s]);
				if(s>=1)
				printf("--->");
			    }
				printf(", ������ %d ��. \n",A[i][j]);		
			}
			}
		}
}




void cmd()//�˵����� 
{   
    int a; 
	int yourchoice;
	int flag=0; 

    printf("\t************��ӭʹ�ú��ϴ�ѧ��У԰����ϵͳ*************\t\n\n");
	map();
	printf("\t*--1.-------------------ѧУ�������----------------------*\t\t\n");
	printf("\t*--2.-------------�鿴һ���㵽�����������·��------------*\t\t\n");
	printf("\t*--3.----------------�����������·��-------------------*\t\t\n");
	printf("\t*--4.----------------------�˳�---------------------------*\t\t\n");
	printf("������:");
        do
		{  	
		   if(!scanf("%d",&yourchoice))	
		      {	
		      		
				  flag=0;
	          }	  
	       else	if(!(yourchoice==1||yourchoice==2||yourchoice==3||yourchoice==4))
	        	{   		
	        		flag=0;
				}
				else
				{
					flag=1;break;
				}
				printf("���棡����������:");
				fflush(stdin);
				//break;
		}while(flag==0);	
	switch(yourchoice)
	{
	case 1:system("cls");map();Search(g);break;//�鿴������Ϣ 
	case 2:system("cls");map(); 
    printf("������������ʼλ�ã�");
     do
		{ 	
		   if(!scanf("%d",&a))	
		      {	   	
		      	flag=0;
	          }	 
	      else 	if(!(a==0||a==1||a==2||a==3||a==4||a==5||a==6))
	        	{
	        		flag=0;
				} 
			else 
			      {
				     flag==1;
				     break;
			       	} 
	    printf("���棡����������������ʼλ�ã�");
	    fflush(stdin);
	}while(flag==0);
	printf("\n") ;
    Dijkstra(g,a);break;//һ���㵽����������·�� 
	case 3:system("cls");map();Floyd(g);break;//��������������·�� 
	case 4:system("cls");exit(1);break;//�˳�ϵͳ 
	default:break;
	}
}


void deal()//���ز˵�||�˳�ϵͳ���� 
{
	int YC;
	int flag=0;
	printf("1:�������˵�\n");
	printf("0:�˳�ϵͳ\n");
	printf("������:");
	 do
		{	
		   if(!scanf("%d",&YC))	
		      {	 
		      	flag=0;
	          }
	      else 	if(!(YC==0 || 1==YC))
	        	{
	        		flag=0;
				} 
				else
				{
					flag==1;break;
				}
		printf("���棡����������:");
		fflush(stdin);
	}while(flag==0);
    switch(YC)
	{
	case 1:system("cls");cmd();break;//�鿴������·��
	case 0:system("cls");exit(1);break;
	default:break;
}
}




 int main()
{
    InitGraph();
    cmd();   
    system("pause");
	return 0;
 }

