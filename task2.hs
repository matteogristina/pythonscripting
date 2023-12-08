import System.Environment

--length :: [a] -> Int
--length []     = 0
--length (_:xs) = 1 + length xs

rgbinvert :: [Int] -> [Int]

rgbinvert [] = []
rgbinvert (x:xs) = [subtract x 255]  ++ rgbinvert xs

main :: IO ()

--A sequence of actions can be combined as a single composite action using the keyword do.

-- Writing a main I/O function 
main = do
    args <- getArgs               -- Command line args are collected as a string 

    -- Command line args are collected as a string
    -- read is an inbuilt function to convert string to int. ::[Int] is the type signature
    let numbers = map read args :: [Int]

    -- Call the function 
        result = rgbinvert numbers

     -- Convert the result back to string 
        resultStrings = map show result
        outputString = unwords resultStrings

     -- print the string 
    putStrLn outputString