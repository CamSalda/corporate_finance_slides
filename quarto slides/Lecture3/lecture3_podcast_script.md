# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 3: The Efficient Frontier and the Best Portfolio

> **Lecture companion.** This episode walks through Lecture 3 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapters 11.2 to 11.5 of Berk and DeMarzo. It is made
> with the open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All
> numbers and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 3: The Efficient Frontier and the Best Portfolio. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapters 11.2-11.5.
- **Topics:** Recap of portfolio risk and return; efficient portfolios with two stocks; the minimum-variance portfolio; short sales; the efficient frontier with many stocks; the risk-free asset and leverage; the Sharpe ratio; the tangency portfolio; systematic and idiosyncratic risk; exercises
- **Length:** 30 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 3 of the Corporate Finance course at ESCP, "The Efficient Frontier and the Best Portfolio." It follows chapters 11.2 to 11.5 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture three. This is the one with the curves, right?

MEI: The curves, one straight line, and the most useful result in the whole course. Here's the plan from the first slide. Recap lecture two. Find the efficient portfolios built from two stocks. Move from two stocks to many: the efficient frontier. Add a risk-free asset and identify the single best risky portfolio, the one the professor calls "super-efficient." And finally, separate the risk that diversification removes from the risk that stays.

MIGUEL: And the formulas?

MEI: Same rule as always for this course. Lecture three has a few pages of algebra: a derivative, a double summation, a square table of covariances. We'll tell you what each block says and why it's there, and point you to the slide. The examples we'll do with numbers, because numbers travel well by ear.

MIGUEL: Then let's start where the lecture starts, with the recap.

## Recap of lecture two

MEI: Eight recap slides, fast. One: a portfolio is the answer to one question, how much of the money goes into each asset? With two assets, you choose the weights, which add up to one. And two assets held together are not the same thing as each on its own: the portfolio's risk depends on how they move relative to each other.

MIGUEL: Two, the framework.

MEI: Investors care about expected return, more is better, and risk, less is better. Every asset is a point on a chart, risk horizontal, return vertical. Two equivalent rules: for a given return, minimize risk; for a given risk, maximize return. And a utility function scores the trade-off: expected wealth minus gamma over two times its variance, where gamma is the risk aversion.

MIGUEL: The three monsters.

MEI: All built from the covariance: for each year, the distance of X from its mean times the distance of Y from its mean, averaged. Positive, they move together; negative, in opposite directions. Correlation: the covariance divided by the two volatilities, always between minus one and plus one. Beta: the covariance divided by the variance of X, how much Y moves when X moves one percent.

MIGUEL: And the portfolio.

MEI: The return is the weighted average of the returns: thirty percent in a stock earning ten and seventy in one earning four gives five point eight. The variance is not an average: it's the two weighted variances plus a comovement term with the covariance, and you can write that term with the correlation times the two volatilities.

MIGUEL: Which is what the last recap slide is about.

MEI: Correlation drives diversification. Correlation one: no diversification, the portfolio's risk is the weighted average of the two risks. Below one, including zero: the portfolio's risk is smaller than the average risk. Negative: strongest diversification, and at minus one the risks subtract exactly, so with the right weights you can bring the risk to zero.

MIGUEL: Then the lecture proper begins.

MEI: With one sentence: lecture two gave us the tools to measure the return and the risk of any portfolio. Today we use them to answer the real question: among all the portfolios we could build, which ones are worth holding?

## A. Efficient portfolios with two stocks

MEI: Two stocks you'll see for the whole lecture. Intel: expected return twenty-six percent, volatility fifty percent. Coca-Cola: expected return six percent, volatility twenty-five. And an assumption that keeps the arithmetic clean: the correlation between them is zero.

MIGUEL: Which portfolio should we choose?

MEI: That's the slide's question. Take an example: forty percent in Intel, sixty in Coca-Cola. Expected return: zero point four times twenty-six plus zero point six times six, fourteen percent. Variance: zero point four squared times zero point five squared, plus zero point six squared times zero point two five squared, plus a covariance term that is zero. That's zero point zero six two five, and the square root is twenty-five percent.

MIGUEL: Twenty-five percent. The same volatility as Coca-Cola alone.

MEI: Hold that thought. The slides then show a table with six portfolios, from all Intel to all Coca-Cola, in steps of twenty percent. All Intel: twenty-six and fifty. Eighty-twenty: twenty-two and forty point three. Sixty-forty: eighteen and thirty-one point six. Forty-sixty: fourteen and twenty-five. Twenty-eighty: ten and twenty-two point four. All Coca-Cola: six and twenty-five.

MIGUEL: Wait. Twenty-eighty has twenty-two point four percent volatility. That's less than Coca-Cola on its own, and it earns ten instead of six.

MEI: And that's the whole idea of the section. Plot the six rows as points and they trace a curve that bends to the left. The professor added a slide where you can see the table turn into the curve. Its upper part is the efficient set.

MIGUEL: Define efficient.

MEI: A portfolio is efficient if it has the minimum variance for a given expected return, or the maximum expected return for a given variance. It's inefficient when you can find another portfolio with a larger expected return and lower or equal volatility. Two questions to ask: is there a portfolio with the same return but lower risk? Is there one with the same risk but higher return? If either answer is yes, your portfolio is inefficient.

MIGUEL: Let's test Coca-Cola. All in Coca-Cola: six percent return, twenty-five volatility.

MEI: The slide draws a dotted line up from twenty-five percent volatility, and it meets the curve twice: once at Coca-Cola, six percent, and once at the forty-sixty portfolio, fourteen percent. Same risk, more than double the return. So holding only Coca-Cola is inefficient.

MIGUEL: Why would anyone hold it alone?

MEI: Nobody should, if these numbers are right. The textbook's figure of the frontier makes the same point: everything on the lower branch of the curve is dominated by a point on the upper branch directly above it.

MIGUEL: And the correlation?

MEI: Shapes the curve. The slide shows the curve for several correlations. At plus one, risk is the weighted average of the two volatilities and the "curve" is a straight line between the two stocks: no diversification. As the correlation falls, the curve bends further to the left: the same returns at lower risk. The gain is largest for negative correlation and maximal at minus one. The conclusion slide: a good way to reduce the risk of a portfolio, or to increase the return you get for every level of risk, is to add assets with a negative correlation.

## The minimum-variance portfolio

MEI: Now the nose of the curve. The minimum-variance portfolio is the combination of the two stocks with the lowest risk: the leftmost point, where the curve turns back. For Intel and Coca-Cola it's twenty percent Intel, eighty Coca-Cola, with twenty-two point four percent volatility, below either stock alone.

MIGUEL: And it matters because?

MEI: Three reasons on the slide. The efficient set begins there: above it the curve is efficient, below it every portfolio is dominated. It ignores expected returns: its weights depend only on volatilities and correlation. And the most cautious investor picks it without even looking at returns.

MIGUEL: Now, how do you find it? I see two slides of algebra.

MEI: Here's the block we promised to describe rather than read. You start from the portfolio variance formula. The two weights add up to one, so you replace the second weight by one minus the first, and the variance becomes a function of a single unknown. Then you ask: which value of that weight makes the variance as small as possible? That's a minimization. You take the derivative, set it to zero, that's the first-order condition, and solve. The result is a formula for the weight of stock one in terms of the two volatilities and the correlation.

MIGUEL: And the expected returns?

MEI: They never appear. That's the point the slide makes after the formula: only volatilities and the correlation matter. And the check with Intel and Coca-Cola, correlation zero: the weight on Intel is Coca-Cola's variance over the sum of the two variances, zero point two five squared over zero point five squared plus zero point two five squared, which is zero point two. The twenty-eighty portfolio.

MIGUEL: So the formula agrees with the table.

MEI: Go look at those two slides with a pencil, it's a ten-minute exercise and it's the kind of thing that comes back. Professor Saldarriaga really went far on this one: the full derivation, step by step, so nobody has to take the formula on faith.

## Short sales

MIGUEL: Then there's a reminder about short sales.

MEI: From lecture two, in one slide: selling a stock you do not own, borrowed from your broker, to buy it back later. You gain if the price falls and lose if it rises, with no ceiling on the loss. In the portfolio formula a short sale is a negative weight, and the weights still add up to one. And why it matters here: negative weights widen the set of portfolios we can build.

MIGUEL: And a step-by-step example.

MEI: Today you borrow one share of stock A worth a hundred, sell it, and put the hundred in the risk-free asset at five percent. In one year your cash has grown to a hundred and five, and you must buy one share of A to return it. The table on the slide: if A rose ten percent, buying it back costs a hundred and ten, you lose five. If A is flat, it costs a hundred, you gain five. Down ten percent, you gain fifteen. Down twenty, you gain twenty-five.

MIGUEL: The lower A goes, the more I make.

MEI: The short position is worth minus the price of the share. Now the exercise with a name: Jérôme has twenty thousand euros for one year. He sells short ten thousand euros of Coca-Cola and uses the proceeds plus his own money to buy thirty thousand of Intel. Correlation still zero. Expected return and volatility?

MIGUEL: Weights first.

MEI: His own money is twenty thousand. Intel: thirty over twenty, one point five. Coca-Cola: minus ten over twenty, minus zero point five. They add up to one. Expected return: one point five times twenty-six, thirty-nine, minus zero point five times six, three: thirty-six percent.

MIGUEL: And the risk?

MEI: Zero correlation, so no covariance term. One point five squared times zero point five squared, zero point five six two five, plus minus zero point five squared times zero point two five squared, zero point zero one five six. Total zero point five seven eight, square root seventy-six percent.

MIGUEL: Thirty-six percent return and seventy-six percent volatility. More than Intel on both counts.

MEI: Which is the lesson: short selling extends the curve beyond Intel. The figure on the next slide shows the frontier continuing past the all-Intel point, up and to the right.

## B. Many stocks: the efficient frontier

MEI: Section B adds a third stock, and the professor picked a deliberately bad one. Meet Bore Industries: expected return only two percent, the same twenty-five percent volatility as Coca-Cola, and uncorrelated with both. On its own it's a poor investment, dominated by Coca-Cola.

MIGUEL: So why add it?

MEI: Because it helps anyway. Mixing Bore with a fifty-fifty Intel-Coca-Cola portfolio gives a new curve that lies to the left of the old one: the same returns at lower risk. Bore's returns are unrelated to the other two, so part of its risk cancels out in the mix.

MIGUEL: And with three stocks there's more than a curve.

MEI: Every combination is now possible, and the portfolios fill a whole region. The efficient frontier is the upper-left edge of that region, further left than the two-stock curve. The figures show the three-stock region, and then three stocks versus ten: each stock added moves the frontier left.

MIGUEL: The summary slide.

MEI: Four points. A portfolio is efficient when no other offers more return for the same risk or less risk for the same return. The efficient frontier is the set of all efficient portfolios, the upper-left edge. More stocks, better frontier: every stock we add, even a poor one on its own, moves it further left, so the best frontier uses all available investments. And efficient portfolios may include short positions. Then one thing still missing: so far every portfolio is made only of risky stocks. What if we can also lend or borrow at a risk-free rate?

MIGUEL: Before that, two slides on the variance with N stocks. The double sum.

MEI: Intuition only, slide for the details. With three stocks the formula has two groups of terms. The own risk of each stock: weight squared times variance, one term per stock. And the comovement: one term for every pair of stocks, with the covariance of the pair, counted twice. With three stocks, three variance terms and three pairs. With fifty stocks, fifty variance terms and one thousand two hundred and twenty-five pairs.

MIGUEL: So the pairs take over.

MEI: That's the sentence in bold: in a large portfolio the risk comes mostly from the covariances, not from each stock's own variance. The second slide shows it as a square table, one row and one column per stock. The variance of the portfolio is the sum of all the cells. The diagonal, N cells, holds the variances. Everything off the diagonal, N squared minus N cells, holds the covariances. In a large portfolio those are the vast majority, and they decide the risk.

MIGUEL: Picture the table and you've understood the formula. Nice.

## C. Adding a risk-free asset

MEI: Section C. Besides diversifying, there's a second way to control risk: keep part of the money in a risk-free asset, a bank deposit or Treasury bills. Its return, the risk-free rate, is known in advance: zero volatility and zero correlation with every stock. And you can do the reverse: borrow at the risk-free rate and invest more than your own money in risky assets. That's leverage, or buying on margin.

MIGUEL: And the example is from Tobin.

MEI: James Tobin, 1958. Next year is either sunny or rainy, each with probability one half. Umbrella Inc loses money in the sun and makes money in the rain: minus ten percent in the sun, plus thirty in the rain. Expected return ten percent, and since each outcome is twenty points from the mean, volatility twenty percent. A bank deposit pays three percent whatever the weather: three percent, zero volatility.

MIGUEL: Step one.

MEI: You have a hundred. Fifty in Umbrella, fifty in the deposit. In the sun: half of minus ten plus half of three, minus three point five percent. In the rain: half of thirty plus half of three, sixteen point five. Expected return six point five percent, volatility ten percent. Both numbers sit exactly halfway between the deposit and Umbrella. Half the money in the risky asset gives half its risk and half its risk premium.

MIGUEL: And leverage?

MEI: The slide defines it: investing with borrowed money, so you control a position bigger than your own cash. The everyday example is a flat worth three hundred thousand euros bought with sixty thousand of your own money and a mortgage of two hundred and forty thousand. You put up twenty percent of the price but you get a hundred percent of its moves: if the flat gains ten percent, your sixty thousand gains fifty percent; if it loses ten percent, half your money is gone.

MIGUEL: Leverage magnifies gains and losses alike.

MEI: It doesn't make an investment better, it scales it up. And in our framework nothing new is needed: borrowing at the risk-free rate is a negative weight on the risk-free asset, with the weight on the risky asset above one.

MIGUEL: Step two, then.

MEI: Borrow fifty at three percent and invest a hundred and fifty in Umbrella: weights one point five and minus zero point five. Sun: one point five times minus ten, minus zero point five times three, minus sixteen point five percent. Rain: one point five times thirty minus zero point five times three, forty-three point five. Expected return thirteen point five percent, volatility thirty.

MIGUEL: One and a half times the risk, one and a half times the risk premium.

MEI: Exactly the slide's words. And now the picture: all the combinations lie on a straight line from the deposit through Umbrella. Lending puts you between the two, borrowing puts you beyond Umbrella. Two short formulas on the slide say why: both the expected return above the risk-free rate and the volatility grow in proportion to the fraction in Umbrella, so every mix is on the same line.

## The Sharpe ratio

MIGUEL: And the slope of that line has a name.

MEI: The Sharpe ratio. The slide does one line of substitution to show it, which you can read, and the result is this: the expected return of any mix equals the risk-free rate plus a slope times the volatility of the mix. The slope is the excess return of the risky investment over the risk-free rate, divided by its volatility. The extra return you earn for each unit of risk you take.

MIGUEL: For Umbrella?

MEI: Ten minus three, over twenty: zero point three five. Every one percent of volatility buys zero point three five percent of return above the risk-free rate.

MIGUEL: And now we can compare risky investments.

MEI: Once a risk-free asset exists, you can combine any portfolio on the frontier with it, and each gives a straight line from the risk-free point. The table on the slide, with a risk-free rate of three percent: Coca-Cola, six percent and twenty-five, Sharpe ratio zero point one two. The twenty-eighty portfolio, ten and twenty-two point four, zero point three one. Fifty-fifty, sixteen and twenty-eight, zero point four six. Intel, twenty-six and fifty, also zero point four six.

MIGUEL: So Intel and the fifty-fifty portfolio pay the same per unit of risk, and Coca-Cola pays almost nothing.

MEI: And the rule: take the highest Sharpe ratio and mix it with the risk-free asset. At any level of risk, it pays more than any other mix, whoever you are. Since leverage makes any return possible, compare Sharpe ratios, not returns.

MIGUEL: There's a figure with two lines.

MEI: The line through Intel, slope zero point four six, and the line through the twenty-eighty portfolio, slope zero point three one. The first is above the second everywhere. Mixing Intel with the risk-free asset beats mixing the twenty-eighty portfolio with it, at every level of risk.

## The tangency portfolio

MEI: And now the best line of all. Rotate the line from the risk-free point upward until it just touches the curve. The touching point is the tangency portfolio: sixty-six percent Intel, thirty-four percent Coca-Cola. Return nineteen point one percent, volatility thirty-four, Sharpe ratio zero point four seven five, the highest available. Every other line lies below it.

MIGUEL: So this is the super-efficient portfolio.

MEI: And here's the result the professor was clearly most excited about, because the slide title says it plainly: everyone holds the same risky portfolio. The tangency line beats every other line, so no investor wants a different risky portfolio. Risk aversion decides only where on the line you sit. Cautious investors put part of their money in the tangency portfolio and lend the rest at the risk-free rate: between the risk-free point and T. Bold investors borrow and put more than their own money in T: beyond T on the line.

MIGUEL: Same portfolio for the nervous and for the brave. Only the dose changes.

MEI: That's the two-fund separation theorem, Tobin again, 1958: every investor holds the same two funds, the tangency portfolio and the risk-free asset, in different proportions. The choice of the risky portfolio is objective; only the mix is personal.

MIGUEL: And with many securities?

MEI: The general picture is the same: the Markowitz curve, the risk-free point, one tangency portfolio. Every other portfolio on the curve stops being efficient once the risk-free asset exists. So the efficient frontier is now a straight line, and its equation reads: risk-free rate, plus a risk premium proportional to the risk you take. The proportion is the Sharpe ratio of the tangency portfolio, the same for everyone. With Intel and Coca-Cola: three percent plus zero point four seven five times the volatility.

MIGUEL: Can we see someone move to the line?

MEI: The example slide. An investor holds the twenty-eighty portfolio: ten percent return, twenty-two point four volatility. Two ways to do better. Same risk, more return: put a fraction x in T so that x times thirty-four equals twenty-two point four, so x is zero point six six, the rest at the risk-free rate. Return: three plus zero point six six times sixteen point one, thirteen point six percent instead of ten.

MIGUEL: And same return, less risk?

MEI: Choose x so that three plus x times sixteen point one equals ten: x is zero point four three. Volatility: zero point four three times thirty-four, fourteen point seven percent instead of twenty-two point four. Either way the investor ends up on the tangent line, holding only T and the risk-free asset.

## Two types of risk

MEI: Last concept of the lecture. Two types of risk. Systematic risk: common to all securities. The slide shows a picture from the global financial crisis. Idiosyncratic risk: specific to one security. The slide shows Boeing.

MIGUEL: And which one does diversification remove?

MEI: That's the question on the next slide, with the variance formula for N stocks written once more, and a hint: not clear? Take equal weights, one over N. With equal weights, each stock's own variance is divided by N squared and fades as N grows; the covariance terms don't fade, because there are more and more of them. So the idiosyncratic part disappears and the systematic part stays.

MIGUEL: And there's a figure.

MEI: Volatility of an equally weighted portfolio against the number of stocks. With one stock, around forty percent. As you add stocks the curve falls fast, and by a hundred stocks it has flattened at about twenty percent and stays there to a thousand. The part that disappears is labelled "elimination of diversifiable risk." The part that stays is "correlated, market, risk."

MIGUEL: So half the risk of a typical stock is just noise you can cancel for free.

MEI: And the summary slide, in two columns. Common risk, market-wide: economic conditions, interest and exchange rates, inflation. The asset is affected by the evolution of the market, with its own sensitivity. That's systematic risk, undiversifiable, market risk. Independent risk, specific to the firm: product market, quality of management, operational risk. That's idiosyncratic risk, diversifiable.

MIGUEL: And the one that stays is the one that should be paid. That's lecture four, I guess.

MEI: That's lecture four.

## The exercises

MIGUEL: The lecture ends with exercises. Let's do the first one, it's fully solved on the slides.

MEI: Exercise one. Stock A trades at a hundred. In one year it's worth a hundred and twenty if the economy expands, probability one half, or a hundred in a recession, probability one half. Risk-free rate five percent. A fund called AlwaysMore claims a product superior to stock A: for two hundred and twenty today, it pays three hundred and twenty in the expansion and two hundred in the recession.

MIGUEL: Question one, stock A.

MEI: Returns: plus twenty percent in the expansion, zero in the recession. Expected return ten percent. Each outcome is ten points from the mean, so the volatility is ten percent. Sharpe ratio: ten minus five, over ten: zero point five zero.

MIGUEL: Question two, the product.

MEI: Expansion: three twenty over two twenty minus one, plus forty-five point five percent. Recession: two hundred over two twenty minus one, minus nine point one. Expected return eighteen point two percent. Each outcome twenty-seven point three points from the mean, so volatility twenty-seven point three. Sharpe ratio: eighteen point two minus five, over twenty-seven point three: zero point four eight.

MIGUEL: More return, much more risk. Is it superior?

MEI: Compare Sharpe ratios: zero point five zero against zero point four eight. The product pays less extra return per unit of risk. Not superior. And you can do better yourself: to reach the product's risk of twenty-seven point three, put two point seven three times your money in stock A, borrowing the rest at five percent. Expected return: five plus two point seven three times five, eighteen point six percent. Same risk as the product, eighteen point six against eighteen point two. Borrowing to buy stock A beats AlwaysMore. Reject the offer at two twenty.

MIGUEL: And question four, the highest price you'd pay.

MEI: The product is just a bundle of stock A and borrowing, so build the bundle that pays exactly three twenty and two hundred. Buy a shares and put b in the risk-free asset. Two equations, one per state. Subtract one from the other: twenty a equals a hundred and twenty, so six shares. Then one point zero five b equals two hundred minus six hundred, so b is minus three hundred and eighty-one: you borrow three eighty-one. Cost today: six shares at a hundred, minus the three eighty-one borrowed, two hundred and nineteen euros.

MIGUEL: And they ask two twenty.

MEI: One euro more than it costs to build yourself. At two nineteen its Sharpe ratio would be exactly zero point five, the same as stock A. That's a beautiful exercise, and the professor solved it on four slides so you can follow every step.

MIGUEL: Exercise two?

MEI: Not solved on the slides, so here's the sketch; do it with the formulas. Two stocks, A with ten percent return and fifteen volatility, B with fifteen and twenty-five, correlation minus zero point three. Forty-sixty: return thirteen percent, and the variance formula gives a volatility of about fourteen point four percent. For an eleven percent return you need eighty percent in A, and the volatility is about eleven point five. And with a risk-free rate of five percent, mix the forty-sixty portfolio, whose Sharpe ratio is much higher than A's, with the risk-free asset: to earn A's ten percent you need about sixty-two percent of it, with a volatility of about nine percent instead of fifteen.

MIGUEL: And the diversification exercise?

MEI: A with twelve percent and fifteen volatility, B with twenty and forty-five. Fifty-fifty with a correlation of zero point two: return sixteen percent, volatility about twenty-five percent. And if they're perfectly negatively correlated, the lowest-risk portfolio has zero risk: seventy-five percent in A and twenty-five in B, the weights in inverse proportion to the volatilities, with a return of fourteen percent.

## Wrap-up: the recap

MIGUEL: Okay. Recap time. The whole lecture in one minute.

MEI: Two stocks trace a curve. Its upper branch is efficient: no other portfolio gives more return for the same risk or less risk for the same return. The curve bends left as the correlation falls. The minimum-variance portfolio is its nose, and its weights depend only on volatilities and correlation, never on returns. Short sales extend the curve.

MIGUEL: Many stocks.

MEI: The portfolios fill a region, and the frontier is its upper-left edge. Every added stock, even a poor one, moves it left. In a large portfolio the risk comes from the covariances, not from each stock's own variance.

MIGUEL: The risk-free asset.

MEI: Mixing a risky portfolio with lending or borrowing puts you on a straight line whose slope is the Sharpe ratio: excess return per unit of risk. The best line is tangent to the frontier, at the tangency portfolio. Everyone holds that same risky portfolio and adjusts the dose with the risk-free asset: two-fund separation.

MIGUEL: Two risks.

MEI: Idiosyncratic risk is specific to a firm and disappears in a diversified portfolio. Systematic risk is common to the market and stays. Only the risk that stays can be rewarded.

MIGUEL: And the quiz questions? Quick answers.

MEI: Leverage effect: investing with borrowed money scales up both risk and risk premium. Diversification effect: combining assets that are not perfectly correlated gives a portfolio risk lower than the weighted average of the risks. Can the risk-free asset raise the return of a portfolio? Yes, by borrowing, and the risk rises in the same proportion. Not perfectly correlated stocks: the portfolio risk is always lower than the weighted average, answer a.

MIGUEL: The second quiz slide.

MEI: Can you fix the level of risk? Yes, by choosing the fraction in the tangency portfolio, since risk is proportional to it. The level of return? Same way. When can it pay to buy a stock with higher risk and lower return? When it's negatively correlated with what you hold, so it lowers the portfolio's risk. Short sales: selling a borrowed share to buy it back later. You bet on the price falling. And a short position is a negative portfolio weight.

MIGUEL: My takeaway: don't pick stocks, pick the tangency portfolio and then decide how brave you are. Also, never pay two twenty for something you can build for two nineteen.

MEI: Read chapters 11.2 to 11.5, redo exercise one with the slides closed, and look at the minimum-variance derivation once with a pencil. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
