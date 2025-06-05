int maxArea(int* height, int heightSize) {
    int smaller(int a, int b){
    if(a<b){
        return a;
    }
        return b;
    }


   int i=0;
   
   int counter=0;
   int j=heightSize-1;
    int ans=0;
    int maxi=0;
    int maxj=heightSize-1;
   while(i!=j){
    
    

    if(height[i]>=height[maxi] || height[j]>=height[maxj]){
        printf("Entered first if i=%d j=%d\n",i,j);
        if(smaller(height[i],height[j])*(j-i)>ans){
            printf("Entered secound if\n");
            ans=smaller(height[i],height[j])*(j-i);
            maxi=i;
            maxj=j;
            printf("maxi=%d maxj=%d max=%d\n/////\n",maxi,maxj,ans);
        }
   }
    if(height[i]<height[j]){
        i++;
    }
    else{
        j--;
    }
    counter++;
   }

   printf("maxi=%d\nmaxj=%d",maxi,maxj);
   
    return ans;
}
