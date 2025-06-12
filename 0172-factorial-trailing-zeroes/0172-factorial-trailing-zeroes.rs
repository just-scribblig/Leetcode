impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut ans:i32 = 0;
        let mut i:i32 = 5;
        while n/i >= 1 {
            ans += n/i;
            i *= 5
        }
        ans
    }
}