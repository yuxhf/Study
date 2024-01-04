#include<stdlib.h>  //包含system等系统调用
#include<stdio.h>
#include<conio.h>  //定义了通过按键盘产生的对应操作
#include<string.h>  //在使用到字符数组时需要使用
#define Infinity      32767       //图的矩阵中A（i，i）记为0，若没有通路，记为INFINITY = 32762 
#define MAXV    100  //最大景点数定为40
#define INF 32767


typedef struct{
	int num;//顶点的编号 
	char name[30];//顶点名称 
	char info[100];//顶点的其他信息 
}VertexType;//顶点的类型 

typedef struct{
	int edges[MAXV][MAXV];//邻接矩阵数组 
	int n,e;//顶点数，边数 
	VertexType vexs[MAXV];//存放顶点的信息 
}MGraph; //完整的图邻接矩阵类型 


MGraph g;
void map();
void Search(MGraph g);
void deal();
void Floyd(MGraph g);
void Dispath(MGraph g,int A[][MAXV],int path[][MAXV]);
void Dispath1(MGraph g,int dist[],int path[],int S[],int v);



 



 MGraph InitGraph()  //初始化无向图  
{
	int i=0,j=0;
	g.n=7;//无向图顶点个数 
	g.e=12;//边数 
	for(i=0;i<g.n;i++)
		g.vexs[i].num=i;
	strcpy(g.vexs[0].name,"教学楼");
	strcpy(g.vexs[0].info,"西安航空学院地标建筑,也是最高的建筑");
	strcpy(g.vexs[1].name,"图书馆");
	strcpy(g.vexs[1].info,"这里藏书百万册,设施良好,环境幽雅,适合潜心读书");
	strcpy(g.vexs[2].name,"球场"); 
	strcpy(g.vexs[2].info,"运动无止境,打球的男孩子都帅");
	strcpy(g.vexs[3].name,"操场");
	strcpy(g.vexs[3].info,"这里很适合散步 恋爱,你懂得");
	strcpy(g.vexs[4].name,"公寓(男)");
	strcpy(g.vexs[4].info,"男孩子的寝室");
	strcpy(g.vexs[5].name,"公寓(女)");
	strcpy(g.vexs[5].info,"女孩子的寝室");
	strcpy(g.vexs[6].name,"餐厅");
	strcpy(g.vexs[6].info,"吃饭的地方不多说");

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




void map()//学校平面图 
{
	printf("\t*******************已激活校园导平面图!*********************\t\n");
    printf("\t...........................................................\t\n");
	printf("\t.             ...........                                 .\t\n");
	printf("\t.             . 1.      .  ..............       .......   .\t\n");
	printf("\t.  ........   .  图书馆 .  .2.  球场    .       .3.   .   .\t\n");
	printf("\t.  . 0.   .   ...........  ..............       .     .   .\t\n");
	printf("\t.  .  教  .                                     .  操 .   .\t\n");
	printf("\t.  .  学  .                                     .     .   .\t\n");
	printf("\t.  .  楼  .    ..........                       .     .   .\t\n");
	printf("\t.  .      .    . 6.餐厅 .                       .  场 .   .\t\n");
	printf("\t.  ........    ..........                       .     .   .\t\n");
	printf("\t                                                .......   .\t\n");
	printf("\t.           .............     .............               .\t\n");
	printf("\t.           . 5. （女   .     . 4.（男）  .               .\t\n");
    printf("\t.           .    公寓   .     .    公寓   .               .\t\n");
	printf("\t.           .............     .............               .\t\n");
	printf("\t...........................................................\t\n");	


}


void Search(MGraph g)
{	
	int i;
	printf("编号\t景点名称\t\t景点简介\t\t\n");
	printf("____________________________________________________________________________\n");
	for(i=0;i<g.n;i++)
	printf("%-10d%-25s%-80s\n",g.vexs[i].num,g.vexs[i].name,g.vexs[i].info);
	printf("____________________________________________________________________________\n");
	printf("\n"); 
	deal();
}



void Dijkstra(MGraph g,int v)//迪杰斯特拉算法 
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
			printf("%s 到 %s 的长度是 %d 米 , 路径是 ",g.vexs[v].name,g.vexs[i].name,dist[i]);
		}
		d=0;
		apath[d]=i;
		k=path[i];
		if(k==-1)
		{ 
			printf("无路径\n");
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



void Floyd(MGraph g)//Floyd算法 
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
		Dispath(g,A,path);//输出最短路径
		printf("\n");
		deal();
}



void Dispath(MGraph g,int A[][MAXV],int path[][MAXV])
{	
    int flag=0;
	int i,j,k,s,q,t;
	printf("请您先输入出发点: ");
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
				printf("请您先输入出发点:");
				fflush(stdin);
		}while(flag==0);
		

	printf("请您的输入目的地：");
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
			    printf("警告！请重新输入您的目的地：");
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
				
				printf("%s  到  %s 的路径是 ",g.vexs[i].name,g.vexs[j].name);
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
				printf(", 长度是 %d 米. \n",A[i][j]);		
			}
			}
		}
}




void cmd()//菜单函数 
{   
    int a; 
	int yourchoice;
	int flag=0; 

    printf("\t************欢迎使用河南大学的校园导航系统*************\t\n\n");
	map();
	printf("\t*--1.-------------------学校景点介绍----------------------*\t\t\n");
	printf("\t*--2.-------------查看一定点到各景点的游览路线------------*\t\t\n");
	printf("\t*--3.----------------两景点间的最短路径-------------------*\t\t\n");
	printf("\t*--4.----------------------退出---------------------------*\t\t\n");
	printf("请输入:");
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
				printf("警告！请重新输入:");
				fflush(stdin);
				//break;
		}while(flag==0);	
	switch(yourchoice)
	{
	case 1:system("cls");map();Search(g);break;//查看景点信息 
	case 2:system("cls");map(); 
    printf("请输入您的起始位置：");
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
	    printf("警告！请重新输入您的起始位置：");
	    fflush(stdin);
	}while(flag==0);
	printf("\n") ;
    Dijkstra(g,a);break;//一景点到各景点的最短路径 
	case 3:system("cls");map();Floyd(g);break;//任意两景点的最短路径 
	case 4:system("cls");exit(1);break;//退出系统 
	default:break;
	}
}


void deal()//返回菜单||退出系统函数 
{
	int YC;
	int flag=0;
	printf("1:返回主菜单\n");
	printf("0:退出系统\n");
	printf("请输入:");
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
		printf("警告！请重新输入:");
		fflush(stdin);
	}while(flag==0);
    switch(YC)
	{
	case 1:system("cls");cmd();break;//查看景点间的路线
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

