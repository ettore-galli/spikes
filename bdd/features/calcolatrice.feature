# content of publish_article.feature

Feature: Calcolatrice RPN
    Una semplice calcolatrice RPN

    Scenario: Esecuzione di una somma
        Given Lo stack è vuoto

        When Immetto 2
        And Immetto 3
        And Premo il tasto + 

        Then Viene mostrato il risultato 5