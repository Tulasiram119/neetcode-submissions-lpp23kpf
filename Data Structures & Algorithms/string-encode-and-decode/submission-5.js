class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let str = ""

        for (let s of strs){
            str += s
            str += "~" 
        }
        return str
    }
        

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let ans = str.split("~")
        ans.pop()
        return ans
    }
}
