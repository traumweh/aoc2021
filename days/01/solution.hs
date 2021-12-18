module Main where

main = do
    content <- readFile "input"
    let linesOfFile = read <$> lines content
    let n1 = task1 linesOfFile
    print n1
    let n2 = task2 linesOfFile
    print n2

task1 :: [Int] -> Int 
task1 n = length (filter (uncurry (<)) (zip n (tail n)))

task2 :: [Int] -> Int
task2 n = task1 (map (\(a, b, c) -> a + b + c) (zip3 n n' (tail n')))
        where n' = tail n