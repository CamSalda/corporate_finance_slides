# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 4: The CAPM

> **Lecture companion.** This episode walks through Lecture 4 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapters 11.6 to 11.8 of Berk and DeMarzo. It is made
> with the open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All
> numbers and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 4: The CAPM. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapters 11.6-11.8.
- **Topics:** Recap of the efficient frontier and the tangency portfolio; the required return of a stock and the beta; the three CAPM assumptions; the market portfolio; the Capital Market Line; the CAPM formula; the Security Market Line; the beta of a portfolio
- **Length:** 28 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 4 of the Corporate Finance course at ESCP, "The CAPM." It follows chapters 11.6 to 11.8 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: The CAPM. Four letters that show up in every finance job interview ever.

MEI: Capital Asset Pricing Model. And this is the lecture where three weeks of portfolio theory pay off. Here's the plan from the first slide. Recap lecture three. Then ask what return a stock must offer to be worth adding to a portfolio: that gives the required return and the beta. Then meet the CAPM: when every investor holds the tangency portfolio, that portfolio is the market itself. And finally use the CAPM to find the risk premium of any stock.

MIGUEL: And the equations? I counted. There are a lot of them.

MEI: Same rule as always. Lecture four has one real derivation, three steps of algebra from an inequality to a formula, and an appendix with a Taylor expansion for the brave. We'll tell you what each block says and why it's there, and point you to the slide. The examples we'll do with numbers.

MIGUEL: Then let's start with the recap. And Mei, it's a long one.

## Recap of lecture three

MEI: Twelve recap slides. Professor Saldarriaga wanted to be very, very sure we remembered lecture three before building on it. And honestly, he's right: everything today rests on it. So let's do it fast.

MIGUEL: Two stocks.

MEI: Choose the weights, they add up to one, and each choice is a portfolio with its own return and risk. Plotted with risk across and return up, all the mixes trace a curve. The example is Intel and Coca-Cola with zero correlation, and yes, Intel and Coca-Cola are back today. Fourth lecture in a row. At this point they're the course mascots.

MIGUEL: Efficient portfolios.

MEI: A portfolio is efficient when no other portfolio gives more return for the same risk, or less risk for the same return. The efficient frontier is the upper part of the curve. Example from the slide: all in Coca-Cola, or forty percent Intel and sixty Coca-Cola, both have twenty-five percent volatility. But the mix returns fourteen percent against six. Holding only Coca-Cola is dominated.

MIGUEL: Correlation.

MEI: Correlation plus one, no diversification, the curve is a straight line between the two stocks. Lower correlation, the curve bends left. Correlation minus one, the risks can cancel completely, and the right weights give zero risk.

MIGUEL: The minimum-variance portfolio.

MEI: The nose of the curve, the lowest risk of all. Here it's twenty percent Intel, eighty percent Coca-Cola, with twenty-two point four percent volatility, below either stock alone. Its weights depend only on the volatilities and the correlation, never on the expected returns.

MIGUEL: Short sales.

MEI: A negative weight: sell a stock you borrowed and put more than your own money in the other one. It extends the frontier. Then from two stocks to N: a third stock turns the curve into a region, and the frontier is the upper-left edge of the region. Every stock you add, even a poor one on its own, pushes the frontier further left.

MIGUEL: The risk-free asset.

MEI: Zero volatility, zero correlation with everything. Mixing a risky portfolio with the risk-free asset puts you on a straight line from the risk-free point. The slide's example: Umbrella, ten percent return and twenty percent volatility, mixed half and half with a three percent deposit, gives six point five percent return and ten percent volatility.

MIGUEL: And leverage is the same line, further out.

MEI: Exactly. Borrow fifty at three percent and put a hundred and fifty in Umbrella: return thirteen point five percent instead of ten, volatility thirty instead of twenty. Leverage scales the risk premium and the risk by the same factor. Gains and losses both magnified. Never judge a return without its risk.

MIGUEL: The Sharpe ratio.

MEI: The slope of that line: expected return minus the risk-free rate, divided by volatility. Extra return per unit of risk. The table on the slide: Coca-Cola alone, zero point one two. The twenty-eighty mix, zero point three one. Fifty-fifty, zero point four six. Intel alone, also zero point four six. A steeper line pays more at every level of risk, whoever you are. So compare Sharpe ratios, not returns.

MIGUEL: And the best line?

MEI: The steepest one from the risk-free point is tangent to the curve. Once a risk-free asset exists, the efficient frontier is that straight line: three percent plus zero point four seven five times the volatility, in the example. The tangency point is the risky portfolio with the highest Sharpe ratio, the super-efficient portfolio. Everyone holds it. Risk aversion only sets where you sit on the line: cautious investors lend part of their money, bold ones borrow. Two-fund separation.

MIGUEL: Last recap slide, the two types of risk.

MEI: Systematic risk is market-wide: the economy, interest rates, inflation. It hits every stock at once, so diversification cannot remove it. Idiosyncratic risk is specific to one firm, and it averages out across many stocks. The figure shows volatility falling as stocks are added and flattening at the systematic level.

MIGUEL: Twelve slides in four minutes. And now the actual lecture.

MEI: Now the actual lecture. The transition slide says it well: lecture three found the best portfolio of risky assets. Today we ask what that implies for the return each stock has to offer.

## Introduction

MEI: The CAPM has five fathers on the slide: Tobin in 1958, Treynor in 1962, Sharpe in 1964, Lintner in 1965, Mossin in 1966.

MIGUEL: Five names, and three photos. And one of the photos is Markowitz, who isn't in the list.

MEI: Markowitz built the frontier, so he earned his place in the picture. Sharpe and Markowitz shared the Nobel prize in 1990, Tobin had his in 1981. The professor clearly enjoyed assembling this wall of fame.

MIGUEL: Why does it matter?

MEI: Because the CAPM is the most widely used model linking risk and return. Most firms use it to measure the cost of capital: the discount rate for projects, for valuations, for regulated prices. When a company decides whether to build a factory, somewhere in the spreadsheet there's a CAPM.

MIGUEL: Outline.

MEI: Three sections. A, required returns: is a stock worth adding to a portfolio? Chapter 11.6. B, from the tangency portfolio to the market portfolio, 11.7. C, the CAPM and how to read it, 11.8.

## A. Required returns

MEI: Section A starts from the Sharpe ratio and asks one question. You hold a portfolio, call it P. Someone offers you a stock, call it A. Should you buy some?

MIGUEL: My instinct says: if A has a good return, yes.

MEI: And the whole section is about correcting that instinct. The answer, in the professor's one sentence: a stock is worth adding only if its expected return pays for the risk it adds to your portfolio. And the risk it adds depends on how it moves with what you already hold, not on how risky it is on its own.

MIGUEL: So it's the correlation story again.

MEI: It's the correlation story made precise. Three steps. One, measure the risk A adds to P. Two, measure what that extra risk is worth. Three, compare with what A actually pays.

MIGUEL: Step one.

MEI: Add a small amount of A to P, a fraction called delta, financed by borrowing at the risk-free rate. The extra return is easy: delta times A's risk premium, meaning its expected return minus the risk-free rate. The extra risk is the interesting part. It is not delta times A's volatility. For a small delta, the portfolio's volatility rises by about delta, times A's volatility, times the correlation between A and P.

MIGUEL: The correlation is right there in the formula.

MEI: Which is the whole point. A stock that moves with your portfolio adds its full risk. An uncorrelated stock adds almost none. A negatively correlated one reduces risk. Where does the formula come from? The appendix at the end of the deck, with a Taylor expansion. We'll come back to that.

MIGUEL: Step two.

MEI: What is that extra risk worth? Here's the clever move. You could take the same extra risk another way: leverage, borrowing to buy more of P. And leverage on P pays P's Sharpe ratio for each unit of risk, that's lecture three. So the extra risk from step one, taken through P instead, would earn that extra risk times the Sharpe ratio of P.

MIGUEL: So that's the benchmark.

MEI: That's the benchmark. A is worth adding when its extra return, from step one, is at least what the same risk would earn through P. The slide writes that as an inequality: delta times A's premium on the left, the extra risk times P's Sharpe ratio on the right.

## In a picture: Intel and Coca-Cola

MEI: Before step three, the professor draws it. Two slides, two charts zoomed in around Intel.

MIGUEL: Setting?

MEI: Your portfolio P is Intel: twenty-six percent return, fifty percent volatility. The stock on offer is Coca-Cola: six percent return, twenty-five percent volatility, uncorrelated with Intel. Risk-free rate three percent.

MIGUEL: And the green line?

MEI: Intel mixed with the risk-free asset, the line from lecture three. Its slope is Intel's Sharpe ratio, zero point four six. Beyond Intel, it's leverage on Intel.

MIGUEL: Then the blue curve.

MEI: Borrow a little at three percent and put it into Coca-Cola, on top of Intel. The dot on the chart is delta equal to twenty percent: return twenty-six point six percent, volatility fifty point three. Now draw a new line from the risk-free rate through that dot. It's steeper than the line through Intel. Sharpe ratio zero point four seven against zero point four six.

MIGUEL: That's a small difference.

MEI: Small, but it's at every level of risk. Adding a little Coca-Cola raises the Sharpe ratio, full stop. And remember what Coca-Cola looks like on its own: six percent return, a quarter of Intel's. It looks like a bad investment next to Intel, and it still improves the portfolio.

## Step 3: from the inequality to the rule

MEI: Now step three, and this is the one block of real algebra in the lecture. Three slides. Here's the rule of the podcast: we give you the intuition, you check the equations on the slides.

MIGUEL: Go.

MEI: Start from the inequality of step two and plug in the extra risk from step one. Delta appears on both sides, so the size of the purchase does not matter: cancel it. Then move P's volatility next to the other risk terms. What's left on the right is a single number, the correlation times A's volatility divided by P's volatility, multiplied by P's risk premium.

MIGUEL: And that single number is?

MEI: The beta. Remember lecture two, the third monster: the covariance of two things divided by the variance of the one that moves. It tells you how much one moves when the other moves by one percent. Here the thing that moves is the portfolio P, and we ask how much A moves with it. If you write the covariance as correlation times the two volatilities, the beta of A with respect to P simplifies to exactly that single number: correlation times A's volatility over P's volatility.

MIGUEL: So the monster from lecture two shows up uninvited.

MEI: It shows up exactly where it's needed. Professor Saldarriaga planted it two lectures ago, and here it pays off. The rule now reads: buy A if A's risk premium is at least beta times P's risk premium. The beta scales P's premium into the premium A must offer.

MIGUEL: And the required return?

MEI: Move the risk-free rate to the right-hand side. The required return of A is the risk-free rate plus beta times P's risk premium. Read it as: risk-free rate, plus the portfolio's premium, scaled by how much A moves with the portfolio.

MIGUEL: Give me the three cases.

MEI: Beta one: A must pay the same premium as P. Beta one half: half the premium is enough, because A adds only half as much risk. Beta negative: A reduces risk, so it's worth holding even below the risk-free rate. And the rule cuts both ways. If A pays at least the required return, buy it. If it pays less, the best move is to short it.

## Example: should we add Coca-Cola to Intel?

MEI: Now the numbers. You hold Intel, twenty-six percent and fifty percent. Treasury bills pay three percent. Coca-Cola: six percent return, twenty-five percent volatility, correlation with Intel zero.

MIGUEL: Beta of Coca-Cola with respect to Intel.

MEI: Correlation zero, times twenty-five over fifty. Zero. Required return: three percent plus zero times twenty-three percent. Three percent.

MIGUEL: And Coca-Cola pays six.

MEI: Six is above three. Yes, buy some. It looks poor next to Intel, a quarter of the return, but being uncorrelated it adds almost no risk, so anything above the risk-free rate is worth having. And lecture three agrees: the tangency portfolio held thirty-four percent of Coca-Cola.

MIGUEL: The slide has a twist.

MEI: The twist is my favorite part. Same stock, same return, same risk, but now suppose the correlation with Intel is zero point five instead of zero. Beta becomes zero point five times twenty-five over fifty, that's zero point two five. Required return: three percent plus zero point two five times twenty-three, which is eight point seven five percent. Coca-Cola pays six. Below eight point seven five. No.

MIGUEL: So nothing about Coca-Cola changed.

MEI: Nothing about Coca-Cola on its own changed. The correlation alone flips the decision. That's the sentence from the start of the section, now with numbers attached.

MIGUEL: And where does this go?

MEI: The last slide of section A is the bridge. The rule holds for any portfolio P. Now, lecture three showed that every investor holds the same risky portfolio, the tangency portfolio. Section B asks what that portfolio must be when everyone holds it, and the answer is: the market. Replace P by the market, and the required return becomes the CAPM.

## B. From the tangency portfolio to the market

MEI: Section B has two questions. Which portfolio P does everyone hold? Lecture three said the tangency portfolio, but which portfolio is that, concretely? And second, what does that imply for each stock's return? Four steps.

MIGUEL: Step one, the assumptions.

MEI: Three of them, each in a box. One: everyone can lend and borrow at the risk-free rate. So the efficient set is the straight line from the risk-free point, tangent to the frontier. Two: everyone shares the same estimates of expected returns, volatilities and correlations. So everyone computes the same frontier and the same tangency portfolio. Three: everyone holds an efficient portfolio. So everyone holds that one tangency portfolio, mixed with the risk-free asset in their own proportion.

MIGUEL: Those are strong.

MEI: The slide says so itself. We look at what they imply first, and at their realism at the end.

MIGUEL: Step two. This is the big one.

MEI: Step two is the heart of the lecture, and it's an argument in words, no algebra. Start with lecture three. If the world had only Intel and Coca-Cola, everyone would hold the tangency mix: sixty-five point seven percent Intel, thirty-four point three percent Coca-Cola. The only difference between investors would be how much of it they hold against the risk-free asset.

MIGUEL: Okay.

MEI: Now add up every investor. Since each one keeps the sixty-five point seven, thirty-four point three mix, the total money held in Intel is sixty-five point seven percent of all the money invested in stocks.

MIGUEL: Right.

MEI: But every share of Intel is held by someone. So the total money held in Intel is also the market value of Intel: its price times the number of shares. Conclusion: Intel's market value must be sixty-five point seven percent of the market, and Coca-Cola's thirty-four point three. The tangency weights are the market-value weights.

MIGUEL: Wait. So we never had to compute the tangency portfolio at all. We just look at market values.

MEI: That's the magic trick. The same argument works with N stocks: the tangency portfolio holds all stocks, each in proportion to its market value. The definition in the box: the market portfolio is the portfolio of all risky assets, each with a weight equal to its market value divided by the total value of the market.

MIGUEL: Example?

MEI: If all stocks together are worth a thousand billion euros and a company is worth sixty billion, its weight in the market portfolio is six percent. And a weight that depends on market value is exactly how the value-weighted indices of lecture one are built: the CAC 40, the S&P 500, the MSCI World. Holding the market means holding an index fund. The second box: in equilibrium, the tangency, super-efficient portfolio is the market portfolio.

MIGUEL: Step three.

MEI: The Capital Market Line, CML. Everyone mixes the market and the risk-free asset. The line containing all those combinations is the CML: expected return equals the risk-free rate plus the market's Sharpe ratio times the portfolio's volatility. It's the tangent line from lecture three, with the market as the tangency point. There's a figure on the slide.

MIGUEL: And step four.

MEI: Step four closes the loop. Take any stock and ask what happens if it did not pay its required return with respect to the market. Suppose it paid more. By section A, adding a little of it to the market would raise the Sharpe ratio. Then the market would not be the best portfolio, and everyone would be buying the stock. Its price would rise until the extra return disappears.

MIGUEL: And if it paid less?

MEI: Shorting a little would raise the Sharpe ratio. Everyone would sell, the price would fall until the gap closes. So in equilibrium no stock can beat or trail its required return. Each pays exactly the risk-free rate plus its beta times the market risk premium. That is the CAPM.

MIGUEL: The slide also calls it a pricing model.

MEI: Because if every asset must satisfy this equation, we can use it to evaluate returns. With today's price, if we know the expected return, we know the expected price. Hence "asset pricing."

## C. The CAPM, and how to read it

MEI: Section C. The formula is in a box: the expected return of stock i equals the risk-free rate plus beta times the market risk premium, where the market risk premium is the market's expected return minus the risk-free rate. And beta is the covariance of the stock with the market, divided by the variance of the market.

MIGUEL: Beta with respect to the market this time.

MEI: With respect to the market, from now on. How much the stock moves when the market moves by one percent. And here's the sentence to memorize: only the part of a stock's risk that moves with the market is paid for. Its idiosyncratic risk earns nothing. Investors can diversify it away for free, so nobody needs to be compensated for it.

MIGUEL: The three cases again?

MEI: Beta one: the market's own premium. Beta zero: just the risk-free rate. Beta negative: below the risk-free rate, because the stock is insurance against market falls.

MIGUEL: And the Security Market Line.

MEI: Draw the CAPM with beta on the horizontal axis and expected return on the vertical. The formula is a straight line, the SML. At beta zero it gives the risk-free rate. At beta one it gives the market's expected return. Its slope is the market risk premium. And since the CAPM holds for every asset, every stock and every portfolio sits on this line. Find its beta, read its expected return.

## Example 1 and Example 2

MEI: Example one. Risk-free rate four percent. Market: expected return ten percent, volatility sixteen. Stock A: volatility sixteen percent, correlation with the market zero point three three.

MIGUEL: Beta.

MEI: Zero point three three times sixteen over sixteen. Zero point three three. Expected return under the CAPM: four percent plus zero point three three times six percent. Six percent.

MIGUEL: And the comparison on the slide?

MEI: Take the CML portfolio with the same risk. Sixteen percent volatility on the CML means one hundred percent in the market: expected return ten percent. Same volatility, ten percent against six. Stock A carries as much risk as the market, but only a third of it is market risk. The rest is idiosyncratic and earns nothing. On the SML, Stock A sits at beta zero point three three, a third of the way from the risk-free asset to the market.

MIGUEL: Example two, the negative beta.

MEI: Stock B has a beta of minus zero point three. Same rates. Expected return: four percent plus minus zero point three times six. Two point two percent. Below the risk-free rate.

MIGUEL: Why would anyone hold it?

MEI: Because B rises when the market falls. It is insurance for the rest of the portfolio, and investors pay for insurance by accepting a lower return. On the SML it sits to the left of the risk-free asset, at beta minus zero point three.

## CML versus SML

MEI: Two slides on a confusion that costs points every year: the CML and the SML are both straight lines, and they're not the same line. There's a table.

MIGUEL: Horizontal axis.

MEI: CML: volatility, total risk. SML: beta, market risk only.

MIGUEL: What sits on it.

MEI: CML: only mixes of the market and the risk-free asset. SML: every stock and every portfolio.

MIGUEL: Slope.

MEI: CML: the Sharpe ratio of the market. SML: the market risk premium.

MIGUEL: And the question each one answers.

MEI: CML: best return for a given total risk. Where you should invest. It comes from lecture three. SML: the return a given asset must pay. What each asset pays. It is the CAPM equation drawn.

MIGUEL: And the next slide puts one stock on both.

MEI: McDonald's. On the left, McDonald's lies below the CML. Its total volatility is fifteen percent, but only part of it moves with the market. The rest is diversifiable and earns nothing, so the stock pays less than a CML portfolio of the same risk. On the right, the same stock sits exactly on the SML, at its beta of zero point four five. Only market risk is paid, and the SML pays it.

MIGUEL: So below one line and on the other, at the same time, and that's not a contradiction.

MEI: Not a contradiction. Different axes. Every stock except the market itself is below the CML, and every stock is on the SML.

## How it all connects

MEI: The professor has a slide called "How it all connects," six points, and it is the whole course so far in six lines. One, lecture three: combining risky stocks traces the efficient frontier. Two, add the risk-free asset: the best mixes lie on the steepest line from the risk-free point, tangent to the frontier, and everyone holds the tangency portfolio. Three, add the three assumptions: everyone holds the same tangency portfolio, so it must be the market.

MIGUEL: Four.

MEI: Four, the CML is that tangent line with the market as tangency point: where every investor sits, more or less far from the risk-free point depending on their taste for risk. Five, the CAPM is what each asset must pay for the market to be the best portfolio. Six, the SML is the CAPM drawn, with beta on the horizontal axis.

MIGUEL: That's a slide to photograph.

MEI: That's a slide to photograph.

## The beta of a portfolio

MEI: One last tool. A portfolio's return is the weighted sum of the returns of its stocks. Covariance is linear, so the beta of a portfolio is the weighted average of the betas of its stocks. There's a one-line formula on the slide.

MIGUEL: Example.

MEI: Danone has a beta of zero point five, Ubisoft one point eight. Risk-free rate four percent, expected market return ten. An equally weighted portfolio: half of zero point five plus half of one point eight, which is one point one five. Expected return: four percent plus one point one five times six. Ten point nine percent.

MIGUEL: The French pair after the American pair. The professor is at least diversified in his examples.

MEI: He is.

## The two summary slides

MEI: Two summary slides. The first is the formula with every symbol named. Expected return of stock i: in equilibrium, also the return investors require to hold it. The risk-free rate: what you earn with no risk at all. The market risk premium: the extra return the market pays above the risk-free rate. Beta: the covariance with the market over the variance of the market, how much the stock moves when the market moves by one percent. In words: the return of a stock is the risk-free rate plus its share of the market premium, and that share is its beta.

MIGUEL: And the second summary slide.

MEI: Four things to remember. The market portfolio is the only efficient portfolio of risky assets; the best you can do at any level of risk is mix it with the risk-free asset, the CML. Only market risk is paid; a stock's premium depends on its beta, and idiosyncratic risk earns nothing, the SML. The assumptions are strong: everyone shares the same estimates, everyone borrows freely at the risk-free rate, and neither is true in practice. And yet the CAPM is the standard tool for the expected return of a stock and the cost of capital of a project.

MIGUEL: And the appendix?

MEI: Two slides proving the step one approximation with Taylor's theorem: define a function of delta, take its derivative, evaluate at zero. The professor was clearly having fun. It is not needed to follow the lecture, but if you ever wondered where "about delta times volatility times correlation" came from, it's there, with every step. Take it as a gift for the curious.

## Wrap-up: the recap

MEI: Lecture four in one minute. Section A, the required return. A stock is worth adding to a portfolio only if its risk premium covers the risk it adds, and that risk depends on its correlation with the portfolio. Write it out and the correlation times the volatility ratio becomes the beta. Required return: risk-free rate plus beta times the portfolio's premium. Coca-Cola next to Intel: yes with zero correlation, no with correlation one half.

MIGUEL: Section B.

MEI: Three assumptions: everyone borrows and lends at the risk-free rate, everyone has the same estimates, everyone holds an efficient portfolio. Then everyone holds the same tangency portfolio, and adding everyone up, that portfolio must be the market, with market-value weights. The Capital Market Line is the mix of market and risk-free asset. And since no stock can beat or trail its required return without prices moving, every stock pays the risk-free rate plus its beta times the market premium. The CAPM.

MIGUEL: Section C.

MEI: The CAPM drawn is the Security Market Line, beta across, return up, slope equal to the market risk premium. Every asset is on it. Only market risk is paid. Beta one third gives six percent, beta minus zero point three gives two point two percent: insurance costs money. CML and SML are different lines with different axes. And the beta of a portfolio is the weighted average of the betas.

MIGUEL: My takeaway: stop asking "is this stock risky?" and start asking "does it move with what I already own?" Also, if you ever meet Intel and Coca-Cola in person, tell them they're famous at ESCP.

MEI: Read chapters 11.6 to 11.8, redo the Coca-Cola example with both correlations, and look at step three once on the slides with a pencil. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
