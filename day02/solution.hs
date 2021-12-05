module Main where

import Text.Parsec

main = do
    content <- readFile "input"
    let (Right directions) = parse parser "" content
    let n1 = task1 directions
    print n1
    let n2 = task2 directions
    print n2

task1 :: [(String,Int)] -> Int 
task1 directions = sum (g "forward") * (sum (g "down") - sum (g "up"))
    where f s = filter (\a -> fst a == s) directions
          g s = map snd (f s)

task2 :: [(String,Int)] -> Int
task2 directions = h * v
    where f = filter (\a -> fst a == "forward")
          ff = filter (\a -> fst (fst a) == "forward")
          g l = map snd (f l)
          h = sum (g directions)
          v = sum (map (\a -> snd a * snd (fst a)) fta)
          fta = ff (zip directions (aims directions)) -- filter tuples with aims

rAims :: [(String,Int)] -> [Int]
rAims [] = [0]
rAims (x:xs) = (a + if fst x == "up" then -snd x else if fst x == "down" then snd x else 0) : rAims xs
    where a:as = rAims xs

aims :: [(String,Int)] -> [Int]
aims directions = reverse (rAims (reverse directions))

parser :: Parsec String () [(String,Int)]
parser = do
    direction <- many1 letter
    space
    n <- read <$> many1 digit
    return (direction,n)
    `sepEndBy` newline
