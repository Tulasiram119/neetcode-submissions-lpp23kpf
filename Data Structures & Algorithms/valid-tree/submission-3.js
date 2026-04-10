class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        if(n == 0 || edges.length == 0){
            return true
        }
        const adj = new Map()
        for(let n1n2 of edges){
            const n1 = n1n2[0]
            const n2 = n1n2[1]
            if(!adj.has(n1)){
                adj.set(n1,[])
            }
            adj.get(n1).push(n2)
            if(!adj.has(n2)){
                adj.set(n2,[])
            }
            adj.get(n2).push(n1)
        }
        const visit = new Set()
        const dfs = (i,prev)=>{
            if(visit.has(i)){
                return false
            }
            visit.add(i)
            for(let j of adj.get(i)){
                if(j == prev){
                    continue
                }
                if(!dfs(j,i)){
                    return false
                }
            }
            return true
        }
        return dfs(0,-1) && visit.size === n
    }
}
