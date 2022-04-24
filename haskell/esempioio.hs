-- main :: IO(Char, Char)
-- main = getChar >>= \p1 -> getChar >>= \p2 -> return (p1, p2)
-- main = getChar >>= (\p1 -> getChar >>= (\p2 -> return (p1, p2)))

get2chr :: IO()
get2chr = getChar >>= (\p1 -> getChar >>= (\p2 -> putChar p2))

get2chr' :: IO()
get2chr' = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putChar p1

putResult :: Char -> IO()
putResult s 
    | s == 'p' = putStrLn "Pippo"
    | s == 'c' = putStrLn "Cicci"
    | otherwise = putStrLn " <<otherwise>> "

putResults :: Char -> Char -> IO()
putResults a b = putResult a >> putResult b


get2chrX :: IO()
get2chrX = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putResults p1 p2

--get2Lines :: IO()
--get2Lines = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putResults p1 p2

main :: IO()
main = get2chrX