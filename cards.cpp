#include <iostream>
#include <string>

enum cardSuit
{
  spades = "A",
  hearts = "B",
  diamonds = "C",
  clubs = "D"
};

enum cardValue
{
  ace = "1",
  two = "2",
  three = "3",
  four = "4",
  five = "5",
  six = "6",
  seven = "7",
  eight = "8",
  nine = "9",
  ten = "A",
  jack = "B",
  queen = "D",
  king = "E"
};

class Card
{
  private:
    cardSuit suit;
    cardValue value;
    std::string unicode;
  public:
    void print() const;
    std::string setUnicode(cardSuit suit, cardValue value);
    cardSuit setSuit();
};

std::string Card::setUnicode(cardSuit suit, cardValue value)
{
  std::string unicode = "\U0001F0";

  unicode.append(suit);
  unicode.append(value);

  return unicode;
}

int main()
{
  
}
