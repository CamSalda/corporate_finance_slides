# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 1: Capital Markets and the Pricing of Risk

> **Lecture companion.** This episode walks through Lecture 1 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapter 10 of Berk and DeMarzo. It is made with the
> open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All numbers and
> examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 1: Capital Markets and the Pricing of Risk. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapter 10.
- **Topics:** The summation sign; realized returns; arithmetic and geometric means; compounding; stock splits and adjusted prices; stock indices; volatility; the historical risk-return trade-off; the low-risk anomaly
- **Length:** 26 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 1 of the Corporate Finance course at ESCP, "Capital Markets and the Pricing of Risk." It follows chapter 10 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture one. The first day. So this is the episode you listen to on the metro, slightly nervous, wondering what you signed up for.

MEI: And by the end of it you'll know. Here's the plan. The lecture has four goals: learn some general concepts, learn how to compute returns, understand how we measure risk, and understand what an index is. It's organized in six sections, A to F. A is a first glimpse at risk and return over a century. B is how to compute returns. C is the historical returns of stocks and bonds. D is how we measure risk. E is the trade-off between the two. And F looks at individual stocks, with a surprise at the end.

MIGUEL: And before section A?

MEI: Before section A, Professor Saldarriaga does something I have never seen in a finance course. He opens with a monster.

MIGUEL: A monster. In a corporate finance class.

MEI: With two pictures of it. One scary, one friendly. The scary one comes first.

## The monster: the summation sign

MIGUEL: Okay, I need to know. What is the monster?

MEI: The Greek letter sigma, the big capital S. The summation sign. The slide says it is a monster you will find along the course several times, and the point of these slides is that by the end you'll find it friendly.

MIGUEL: I have to say, I was expecting to be scared of this course, and instead the professor is the one warning me about the scary parts. That's very kind.

MEI: It's a nice touch. And the idea is simple. The symbol is the Greek letter S, and S stands for sum. It is a shortcut for writing a long addition. Instead of writing one plus two plus three plus four plus five, you write the sigma with a few decorations around it. Both mean exactly the same thing: fifteen. The slide puts it well: the symbol saves ink, nothing more.

MIGUEL: So what are the decorations?

MEI: Three things are attached to it. Below the sigma, where to start counting, for instance i equals one. Above it, where to stop, for instance five. And to the right, what to add, the recipe. You take the recipe, put in i equals one, then i equals two, and so on until you reach the number on top, and you add up everything you wrote.

MIGUEL: And the recipe can be anything.

MEI: Anything. The slides show the squares of the first four numbers: one plus four plus nine plus sixteen, thirty. And then the one that matters for finance: the recipe is a cash flow to be discounted. Cash flow in year one divided by one plus r, plus cash flow in year two divided by one plus r squared, plus cash flow in year three divided by one plus r cubed. That's a present value, written with one symbol.

MIGUEL: What if I don't know how many years there are?

MEI: Then you call that number n and write n on top. Start at the first year, stop at year n, add up every discounted cash flow in between. A project paying for five years has n equal to five, one paying for thirty years has n equal to thirty. The formula does not change, only where you stop.

MIGUEL: And the infinity sign on top? That one does look like a monster.

MEI: That's when the payments never stop. A company expected to pay a dividend every year forever. And here's the part the professor clearly enjoyed explaining: adding infinitely many numbers does not have to give an infinite total. Each term is smaller than the one before, because you divide by one plus r once more every year. The terms shrink fast enough that the total settles on a finite number. That's the perpetuity, and it's why a share paying dividends forever still has a finite price.

MIGUEL: I'm not sure I believe that an endless sum can be finite.

MEI: The slide has a simpler example. Keep adding halves of what is left: one half, plus one quarter, plus one eighth, plus one sixteenth, and so on. After two terms you're at zero point seven five. After three, zero point eight seven five. After four, zero point nine three seven five. The total never passes one. It just gets closer and closer.

MIGUEL: Okay. That one I believe. The monster is tamed.

MEI: That's the exact title of the last bullet. And now, section A.

## A. Risk and return: a first glimpse

MEI: Section A is one big picture, Figure 10.1 of the textbook. Imagine you invested a hundred dollars at the end of 1925 in each of several things, and you look at what you have today, with interest and dividends reinvested and transaction costs ignored.

MIGUEL: What things?

MEI: Six series. The S&P 500: ninety US stocks up to 1957 and five hundred after that, leaders in their industries and among the largest firms. Small stocks: the stocks on the New York Stock Exchange in the bottom twenty percent by market capitalization. The MSCI World Index, the world portfolio. Corporate bonds: long-term, triple-A rated US corporate bonds with maturities of about twenty years. Treasury bills: three-month government paper, the safest thing there is. And the CPI, the consumer price index, so you can see inflation.

MIGUEL: And the result?

MEI: A hundred dollars in small stocks became about ten million dollars. In the S&P 500, about one point three million. In the world portfolio, about four hundred thousand. In corporate bonds, about twenty-seven thousand. In Treasury bills, about two thousand one hundred. And the CPI went from a hundred to about one thousand five hundred.

MIGUEL: Wait. So Treasury bills turned a hundred into two thousand, and prices went up fifteen times. The safest investment barely beat inflation in a century.

MEI: Barely. And small stocks beat everything by a mile. But look at the chart more closely, because the professor put the crashes on it. From 1928 to 1932, small stocks lost ninety-two percent and the S&P 500 lost eighty-four percent. In 1937 and 38, minus seventy-two and minus fifty. From 1968 to 74, minus sixty-three and minus thirty-seven. In 1987, minus thirty-four and minus thirty. From 2007 to 2009, minus sixty-seven and minus fifty-one. In 2020, minus fifty and minus thirty-three.

MIGUEL: So the line that ends at ten million is also the line that loses ninety percent from time to time.

MEI: That's the whole course in one sentence: the highest return comes with the biggest swings. And the next figure, 10.2, makes the same point another way. It shows the value of a hundred dollars invested in different years, for horizons of one, five, ten and twenty years. Over one year, stocks are all over the place, sometimes well below a hundred. Over twenty years they almost always come out ahead, but not always by the same amount, and in a few starting years bonds did about as well.

MIGUEL: So time helps, but it is not a guarantee.

MEI: Keep that for the quiz. Section B.

## B. Common return measures

MEI: Section B asks a practical question: how do you determine the return of a financial asset? The list on the slide: returns from dividends and capital gains, calculations with reinvested dividends, stock market indices, histograms of historical returns, historical volatility, and arithmetic versus geometric mean.

MIGUEL: Start with the simplest. One stock, one year.

MEI: The realized return of a stock between two dates has two parts: the capital gain and the dividend. The formula on the slide says the return is your wealth at the end divided by your initial investment, minus one. Spelled out: the end price, plus the dividend, minus the starting price, all divided by the starting price. And you can split it in two pieces: the price change over the starting price, that's the capital gain rate, plus the dividend over the starting price, that's the dividend yield.

MIGUEL: So return equals capital gain rate plus dividend yield.

MEI: And there's a real example of a dividend on the slides: BNP Paribas. A dividend of two euros seventy is detached from the share price on the thirtieth of May 2017, and you can see the price drop that day on the chart.

MIGUEL: Because the cash left the company and went to the shareholders.

MEI: Exactly. Now the part where students get tricked, and the professor built the trap very carefully. How do you calculate the average return on an investment over several years?

MIGUEL: Add the yearly returns and divide. No?

MEI: Look at the table. Investment one goes from a hundred to fifty to a hundred. Returns: minus fifty percent, then plus a hundred percent. Arithmetic average: plus twenty-five percent a year.

MIGUEL: But I started at a hundred and I ended at a hundred. I made nothing.

MEI: Nothing. Investment two goes from a hundred to a hundred and ten to a hundred and twenty-one. Plus ten, plus ten. Average ten percent. And this one actually made money. So the slide concludes, with three dots: the arithmetic average is misleading.

MIGUEL: Okay, so what's the right average?

MEI: The geometric mean, also called the CAGR, the compound annual growth rate: the constant yearly return that turns the initial investment into the final wealth. Two ways to write it, both on the slide. Take the final wealth over the initial investment, raise it to the power one over n, where n is the number of years, and subtract one. Or multiply all the one plus R terms together, raise the product to the power one over n, and subtract one.

MIGUEL: For investment one, that gives a hundred over a hundred, to the power one half, minus one. Zero.

MEI: Zero. Which is the truth. So the rule on the "to sum up" slide: for the average return of one investment over time, use the geometric mean, which is also the internal rate of return of the investment. For the mean return of many investments at one date, or for an expected return, use the arithmetic mean.

MIGUEL: And the two are related?

MEI: Three facts. The two means are equal if annual returns are constant. Otherwise the arithmetic mean is always larger than the geometric mean. And the geometric mean is approximately the arithmetic mean minus one half of the variance. Keep that last one: the more a return bounces around, the more the compound return falls below the simple average. That's the price of volatility.

MIGUEL: Next slide is compounding.

MEI: Returns over several periods must be compounded to get the return over the whole horizon. The example: four consecutive periods with returns of six point one percent, minus five point three two, six point seven two and eight point nine three. You multiply one point zero six one by zero point nine four six eight by one point zero six seven two by one point zero eight nine three, and subtract one. That gives sixteen point seven percent.

MIGUEL: And if I just added them?

MEI: You'd get a different number, and the slide is firm about it: you must not take the sum of the returns. One more remark from the slide: the length of the periods does not matter here. Months, quarters, years, you multiply the same way.

MIGUEL: Then there's a table about Total.

MEI: The Total stock in 2016. Price forty euros eighty-nine on the first of January, forty-eight seventy-two on the thirty-first of December, and four dividends of sixty-one cents along the way. The slide gives the return of each sub-period: two point five seven percent, four point two three, minus two point five seven, eighteen point two five, and two point three five. The question is the total return for the year, and the method is what we just said: multiply the one plus R terms, then subtract one.

MIGUEL: And that gives about twenty-six percent.

MEI: About twenty-six. Try it yourself with the table, it's a good five minutes of practice. Then come stock splits.

MIGUEL: The thing where you suddenly own three times more shares.

MEI: And each is worth a third. Companies sometimes do stock splits, or reverse stock splits, and you must take them into account. The example is CIGNA. You buy a hundred shares on the fifth of August 2006 at a hundred and fifty-five dollars fifty-nine. One year later the stock is worth fifty dollars eighteen. Looks like a disaster.

MIGUEL: Minus two thirds.

MEI: Except the company did a three-for-one split, so you now own three hundred shares. Plus eight dollars fifty of dividends in total. So your end wealth is three hundred times fifty eighteen, plus eight fifty, and your return against a hundred times one fifty-five fifty-nine is minus three point two percent.

MIGUEL: From minus sixty-seven to minus three. The split was the whole story.

MEI: Which is why we use adjusted prices. The slide explains that the big charts from section A don't follow a specific stock price, they follow the value of an investment in the stock. That's a performance index, built with adjusted prices. The adjusted price accounts for dividends and splits, and it's computed so that the last value is today's actual price and the earlier values mirror the evolution of an investment.

MIGUEL: Give me the Coca-Cola one, I like that example.

MEI: On the second of January 1970, Coca-Cola traded at eighty-two dollars twenty-five. On the thirtieth of June 2017, at forty-four dollars eighty-five. Good or bad investment?

MIGUEL: On those two numbers, terrible.

MEI: But Coca-Cola did five stock splits and paid many dividends. The adjusted close for January 1970 is zero point eight five dollars. So the return over 1970 to 2017 is forty-four eighty-five over zero point eight five, minus one: five thousand one hundred and seventy-six percent. And the geometric annual mean is that ratio to the power one over forty-seven, minus one: eight point eight percent a year.

MIGUEL: Professor Saldarriaga really went far on this one. Forty-seven years, five splits, and the stock looks like it halved when it actually multiplied by fifty.

MEI: It's the best illustration of adjusted prices I know. Now, indices.

## Stock price indices

MEI: A stock index aggregates the evolution of a whole exchange by following a portfolio of stocks. The names you know: the CAC 40, the DAX, the S&P 500, the FTSE 100, the Footsie, the Nasdaq 100, the Dow Jones Industrial Average, the Hang Seng, the Nikkei 225. Some are very old. The Dow Jones has been published since 1896 in New York.

MIGUEL: And the attention sign on the slide?

MEI: An important one. These indices can be calculated as a total return index, including dividends, or as a price index, without dividends. And some indices exist in different versions. The table on the next slide sorts them. Gross total return, with dividends reinvested: the DAX 40 in Germany, and the Ibovespa in Brazil. Price only: the S&P 500, the Dow Jones, the Nasdaq, the FTSE 100, the Nikkei 225, the CAC 40, the Hang Seng.

MIGUEL: So when the news says the CAC 40 is flat over ten years, that's without dividends.

MEI: Without dividends. A price index: when a company pays a dividend, its share price drops, and the index does not add the cash back. A total return index assumes every dividend is reinvested, before tax, so it grows faster over time. Most price indices also have an official total return version, like the S&P 500 TR or the CAC 40 GR.

MIGUEL: And there's a third version?

MEI: The slide "the same index comes in three versions." Price index, which we said. Gross total return index, dividends reinvested before any tax: the DAX as quoted in the news, the S&P 500 TR, the CAC 40 GR. And the net total return index, dividends reinvested after the withholding tax a foreign investor would pay: the usual benchmark for international funds and ETFs, like MSCI World Net or S&P 500 Net. Same companies, same prices in all three. The only difference is what happens to the dividends, and over the long run that difference is large.

MIGUEL: How large?

MEI: There's a chart of the CAC 40 against the CAC 40 GR. Same forty companies. The gross return line ends far above the price line. That gap is just dividends, reinvested, over the years.

## C. Historical returns of stocks and bonds

MEI: Section C. And here comes our friend the monster, for real this time. The annual mean return is one over T times the sum of the returns from year one to year T. Which the slide also writes out in full: one over T times the sum of R one plus R two and so on up to R T.

MIGUEL: Start at one, stop at T, add the returns, divide by T. The monster just means average.

MEI: Just means average. And the averages, 1926 to 2021, in the table: small stocks eighteen point six percent a year. The S&P 500 twelve point two. Corporate bonds six point two. Treasury bills three point three.

MIGUEL: Consistent with the ten million dollars.

MEI: Consistent. Then the slide shows the histograms of yearly returns for each portfolio. Treasury bills are a narrow spike near zero. Corporate bonds a bit wider. The S&P 500 spreads from big losses to big gains. And small stocks spread the widest of all, with years above a hundred percent and years below minus fifty.

MIGUEL: The wider the histogram, the scarier the ride.

MEI: And the next section measures the width.

## D. Common measures of risk

MEI: Section D. The slide starts honestly: there is no perfect and generally accepted risk measure. In finance, risk is measured by volatility, and volatility is the standard deviation of returns.

MIGUEL: How do I compute it?

MEI: Two steps. First the variance: take each year's return, subtract the mean return, square the difference, add up all the squared differences, that's the monster again, and divide by T minus one. Then take the square root of the variance, and that's the volatility, written sigma.

MIGUEL: Why T minus one and not T?

MEI: That's a statistics detail; it corrects for the fact that you estimated the mean from the same data. The slide just states the formula. Two warnings, though. Volatility is a symmetric risk measure: it counts the risk to win as well as the risk to lose. A stock that jumps up a lot is volatile too. Other measures capture only the risk of losses, the downside risk, for instance the VaR, the value at risk.

MIGUEL: So volatility is the standard measure, but not the only one, and it doesn't care about direction.

MEI: Right. Section E.

## E. The historical risk and return trade-off

MEI: Now the table that puts return and risk side by side. Volatility, 1926 to 2021: small stocks thirty-eight point six percent. The S&P 500 nineteen point seven. Corporate bonds six point three. Thirty-day Treasury bills three point one.

MIGUEL: And next to it?

MEI: The excess return: the average return in excess of Treasury bills. Small stocks fifteen point three percent. The S&P 500 eight point nine. Corporate bonds two point nine. And the slide defines it: excess return equals the return in excess of the risk-free rate, equals the risk premium.

MIGUEL: So the risk premium is what you're paid for the volatility.

MEI: Put the four portfolios on a chart with volatility on the horizontal axis and average return on the vertical axis, Figure 10.6, and they line up almost on a straight line. Treasury bills bottom left, then corporate bonds, then the S&P 500, then small stocks top right. More volatility, more return.

MIGUEL: That's a beautiful result. Risk is paid.

MEI: For big portfolios, yes. Now hold on to your hat for section F.

## F. Risk and returns of individual stocks

MEI: Figure 10.7 adds individual stocks to the same picture: five hundred S&P 500 stocks, each one a dot, with its volatility and its average return. The large portfolios still sit on the line. The individual stocks don't.

MIGUEL: Where are they?

MEI: All over the place, and almost all of them below the line. Individual stocks have much higher volatility than the portfolios, thirty, forty, fifty percent, but not higher returns. A stock with fifty percent volatility often earns less than the S&P 500 with twenty.

MIGUEL: So for a single stock, more risk does not mean more return.

MEI: That's the puzzle this course spends the next lectures solving. The hint is already in the chart: the portfolios are on the line, the single stocks are not. Something about holding many stocks together removes risk without removing return. That's diversification, and it's where the course goes next.

MIGUEL: And the "what's new" slides?

MEI: The low-risk anomaly, from a 2011 paper by Baker, Bradley and Wurgler. They sort stocks every month by their past volatility into five groups, and track one dollar invested in each group from 1968. The bottom group, the least volatile stocks, turns one dollar into tens of dollars by 2008. The top group, the most volatile stocks, ends up with less than the dollar you started with.

MIGUEL: Less than a dollar. In forty years. The boring stocks won.

MEI: And the second chart shows the same thing holds among the thousand largest firms, so it's not a small-stock oddity. The professor put "new" in quotation marks, because the paper is from 2011, but it's new relative to the textbook's line from section E.

MIGUEL: He was clearly excited about that one. It's the last thing before the quiz.

MEI: I think he wanted you to leave the first lecture with a question, not just a table.

## Wrap-up: the recap

MIGUEL: Okay. Recap time. The whole lecture in one minute, section by section.

MEI: The monster. The summation sign means "add these up": start below, stop above, recipe on the right. An endless sum of shrinking terms is finite, which is why a perpetuity has a price.

MIGUEL: A.

MEI: A hundred dollars in 1925 became about ten million in small stocks, one point three million in the S&P 500, two thousand in Treasury bills, and prices rose fifteenfold. The best performers also had the deepest crashes.

MIGUEL: B.

MEI: Return equals capital gain rate plus dividend yield. Average over time with the geometric mean, not the arithmetic one. Compound returns by multiplying one plus R, never by adding. Adjust prices for dividends and splits, or Coca-Cola looks like it halved when it multiplied by fifty. And an index is a portfolio: price index without dividends, total return index with them.

MIGUEL: C, D and E.

MEI: Average returns since 1926: small stocks eighteen point six, S&P 500 twelve point two, corporate bonds six point two, Treasury bills three point three. Risk is volatility, the standard deviation of returns. Volatility: thirty-eight point six, nineteen point seven, six point three, three point one. Excess return over Treasury bills is the risk premium, and for big portfolios it rises with volatility.

MIGUEL: F.

MEI: Individual stocks break the line: more volatile, not more rewarded. And low-volatility stocks have beaten high-volatility stocks for decades. Diversification is the missing piece.

MIGUEL: And the quiz? Let's do the first three.

MEI: Question one. A stock is worth one dollar at the start of the year. There's a reverse split of one for ten, a dividend of three cents before the split, and the stock ends at eleven dollars. Your one share became a tenth of a share, worth one dollar ten, plus three cents of dividend: one dollar thirteen. Return: thirteen percent.

MIGUEL: Question two: the value halves in six months.

MEI: Return over six months: minus fifty percent. Annualized: one half times one half, minus one: minus seventy-five percent. Compounding works on the way down too.

MIGUEL: Three: minus twenty then plus twenty.

MEI: Arithmetic average: zero. Geometric: zero point eight times one point two is zero point nine six, square root, minus one: about minus two percent. You lost money, and only the geometric mean tells you.

MIGUEL: And the banker who says stocks always beat Treasury bills?

MEI: Figure 10.2: over one year, often not; over twenty years, almost always, but not always. And even if they usually do, that's not by itself a reason to invest: the extra return is the price of the risk, not a free gift. Can volatility be negative? No, it's a square root. Is a riskier stock always a higher-return stock? Figure 10.7 says no.

MIGUEL: Last two, the critical thinking ones.

MEI: A bond bought at ninety-seven, with a four point five coupon on a hundred of nominal, worth a hundred and two at year end. Return: a hundred and two plus four point five minus ninety-seven, over ninety-seven: about nine point eight percent. Same formula as a stock, the coupon plays the dividend. And a stock price up ten percent while the return on equity is minus thirty: no contradiction. The return on equity is an accounting profit on book equity for the past year. The price reflects what investors expect for the future, and a loss that was smaller than feared can be good news.

MIGUEL: My takeaway: returns multiply, risk is a standard deviation, and the monster is just an addition. Also, do not trust two prices forty-seven years apart.

MEI: Read chapter 10, redo the Total and Coca-Cola examples with a calculator, and bring the monster to lecture two. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
