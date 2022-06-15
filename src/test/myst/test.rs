fn main() {
    let mut a = 1; 
    let b = &mut a; 

    println!("{}", a);
    println!("{}", b);
    
    a = 2; 

    println!("{}", a);
    println!("{}", b);
    
    
}