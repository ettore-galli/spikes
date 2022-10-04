import Text.Read



-- get2chr :: IO()
-- get2chr = getChar >>= (\p1 -> getChar >>= (\p2 -> putChar p2))

-- get2chr' :: IO()
-- get2chr' = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putChar p1

-- putResult :: Char -> IO()
-- putResult s 
--     | s == 'p' = putStrLn "Pippo"
--     | s == 'c' = putStrLn "Cicci"
--     | otherwise = putStrLn " <<otherwise>> "

-- putResults :: Char -> Char -> IO()
-- putResults a b = putResult a >> putResult b


-- get2chrX :: IO()
-- get2chrX = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putResults p1 p2

-- --get2Lines :: IO()
-- --get2Lines = getChar >>= \p1 -> getChar >>= \p2 -> putChar p2 >> putResults p1 p2

extract :: Maybe String -> String
extract (Just x) = show x
extract Nothing = "null"


transform :: String -> String
transform t = "[" ++ t ++ "]"

main :: IO()
-- main = putStrLn   (extract (readMaybe >>= getLine) :: Maybe Int)
main = getLine >>= (\userInput ->  putStrLn ( transform userInput))