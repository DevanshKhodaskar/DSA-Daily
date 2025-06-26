public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        helper(0,0,n*2,"",n,ans);
        return ans;
    }

    private void helper(int oc,int cc,int slength,String soln,int n,List<String> ans) {
        if (slength == 0) {
            ans.add(soln);
            return;
        }

        if (oc>cc && cc<n) {
            helper(oc,cc+1,slength-1,soln + ")",n,ans);
        }

        if (oc<n) {
            helper(oc+1,cc,slength-1,soln+"(",n,ans);
        }
    }
}