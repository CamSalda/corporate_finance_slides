# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 2: Portfolio Choice and Diversification

> **Lecture companion.** This episode walks through Lecture 2 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapters 10.5, 10.6 and 11.1 of Berk and DeMarzo. It is
> made with the open-source tools of The Finance and Economics Papers Podcast, for the students of the course.
> All numbers and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 2: Portfolio Choice and Diversification. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapters 10.5-10.6 and 11.1.
- **Topics:** Recap of returns and risk; choice under risk; the mean-variance framework; covariance, correlation and beta; the risk of a two-stock portfolio; diversification; short sales; a worked example
- **Length:** 25 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format. Instead of a paper, we walk through a lecture: Lecture 2 of the Corporate Finance course at ESCP, "Portfolio Choice and Diversification." It follows chapters 10.5, 10.6 and 11.1 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture two. The one where the monster comes back.

MEI: Three monsters, this time. The professor promised in lecture one that the summation sign would return, and he kept his word: lecture two opens with a page of recap slides, then introduces three new creatures, the covariance, the correlation and the beta, and ends with a worked example where you compute all of them by hand.

MIGUEL: That sounds like a lot of formulas.

MEI: It is, and here's how we'll handle them. This lecture is heavy with equations, and a podcast is a bad place to read equations aloud. So for each block of formulas we'll tell you what it says in words and what it's for, and then send you to the slide to look at the actual thing. The numbers in the examples, those we'll do together, because numbers work fine aloud.

MIGUEL: Deal. What's the plan of the lecture?

MEI: Three goals on the first slide: recap what we learned in lecture one, returns and risk; understand how combining assets reduces risk, that's diversification; and learn how to compute the risk and return of a portfolio. The key concepts: covariance and correlation between two stocks, and which risk disappears in a portfolio and which does not.

MIGUEL: Then let's start where the lecture starts, with the recap.

## Recap of lecture one

MEI: Eight recap slides, quick. First the summation sign: a shortcut for a long addition. Below it where to start, above it where to stop, to its right what to add. If you don't know how many terms there are, you call that number T and stop there.

MIGUEL: The monster, tamed.

MEI: Second, why returns. A share of LVMH costs a few hundred euros, a share of Orange about ten. The prices alone say nothing about which was the better investment. The return puts every investment on the same scale: the percentage increase in value for every euro invested. Buy at fifty, sell at fifty-five: each euro became one euro ten, a return of ten percent, whatever the size of your investment.

MIGUEL: And the dividend?

MEI: Third slide. A stock pays you in two ways: its price moves, and it may pay a dividend. The return counts both: end price plus dividend minus starting price, over the starting price. That splits into the capital gain plus the dividend yield. Bought at fifty, sold at fifty-three, dividend of two: capital gain three over fifty, six percent, dividend yield two over fifty, four percent, total ten.

MIGUEL: Fourth: compounding.

MEI: After several periods you earn interest not only on the principal but on the interest already earned. One euro becomes one plus R one, then that grows by one plus R two, and so on. With returns of six point one, minus five point three two, six point seven two and eight point nine three percent, multiplying the four one-plus-R terms gives sixteen point seven percent.

MIGUEL: And there's a chart with a thousand euros.

MEI: A thousand euros invested at ten percent for a long time. Of the twenty-eight thousand one hundred and two euros you end up with, only a thousand is your own money and three thousand five hundred is interest on it. The other twenty-three thousand six hundred and two euros is interest earned on past interest.

MIGUEL: That is the most motivating chart in the course. Compounding does most of the work while you sleep.

MEI: Next, the geometric mean, or CAGR: the constant yearly return that would have produced the same final wealth. For our four periods, one point one six seven to the power one quarter, minus one: three point nine four percent per period. Earn that four times in a row and you get back exactly sixteen point seven.

MIGUEL: Stock splits.

MEI: The company replaces each old share by several new ones. The price per share falls but nothing of value changed: more, smaller slices of the same pie. A hundred shares at a hundred and fifty, a three-for-one split, the price drops to fifty. Looking at the price alone you'd think you lost sixty-six point seven percent. Looking at your position, three hundred times fifty against a hundred times a hundred and fifty: zero percent.

MIGUEL: Always compare the whole position, not the price of a single share.

MEI: Then the arithmetic mean. The geometric mean describes what happened. To say what we expect next year we use the arithmetic mean: add the returns, divide by how many there are. Our four returns give four point one one percent, against a geometric mean of three point nine four. The arithmetic mean is always the larger of the two, unless every return is identical, and from now on it's what we call the expected return, E of R.

MIGUEL: And volatility.

MEI: Risk is about how far the actual return lands from its average. The variance: take each year's distance from the mean, square it so gains and losses both count, and average. The square root is the volatility, in percentage points, so you can read it next to the mean return. Volatility is symmetric: a good surprise counts exactly like a bad one.

MIGUEL: And the last recap slide is the two charts from lecture one.

MEI: Side by side. Large portfolios: a clear link, more volatility, more return. Individual stocks: no clear link, many of them carry a lot of risk for no extra return. Why? Part of the risk of a single stock disappears when it is held together with others, and is therefore not rewarded. The slide ends in bold: that is what this lecture is about.

## Introduction: choosing under risk

MEI: The lecture proper opens with a sentence I like. Today we study the basis of portfolio choice. It can look abstract and distant at first, but it is the basis on which investment decisions are made every day, and on which a sector of trillions of euros operates.

MIGUEL: No pressure.

MEI: And a photo: Harry Markowitz, who pioneered optimal portfolio choice in his article "Portfolio Selection," published in the Journal of Finance in 1952. Nobel Memorial Prize in 1990.

MIGUEL: Nineteen fifty-two. So this lecture is seventy-four years old and still the first thing you learn.

MEI: Because it works. Now the game the professor plays with the class. Do you prefer A, win a hundred thousand euros for sure, or B, a lottery that pays zero with probability one half and two hundred thousand with probability one half?

MIGUEL: A. Obviously A. I'd take the sure hundred thousand and never look back.

MEI: And that's the point. Compute the expected gains: A gives a hundred thousand. B gives one half times zero plus one half times two hundred thousand: also a hundred thousand. By the expected value criterion you should be indifferent. And still, in general, people prefer the sure outcome. That's aversion to risk, and the mean-variance framework is built to handle it.

MIGUEL: How?

MEI: We assume investors care about two things only: return, and risk measured by the variance. Two rules, in two boxes on the slide. Same return, different risk: pick the less risky asset. Same risk, different return: pick the higher return. The slide says these two rules are equivalent, they describe the same investor, one who wants more return and less risk.

MIGUEL: So every asset becomes a point on a chart.

MEI: Expected return on the vertical axis, risk on the horizontal axis. Risk is the standard deviation, the square root of the variance, so both axes are in percent. The chart on the slide shows a few assets as points, and you choose among them by moving up and to the left.

MIGUEL: Up for return, left for less risk.

MEI: Two more slides formalize this. First, final wealth is a random variable: when you invest you don't know today how much you'll end up with, you can only estimate the probability distribution. Two numbers summarize a distribution, its first two moments: the mean, what you get on average, and the variance, how spread out the results are. The sure hundred thousand and the lottery have the same mean but the lottery has a much larger variance.

MIGUEL: And the utility function?

MEI: A score of how satisfied an investor is with a risky investment. It goes up with expected wealth and down with its variance. The common specification on the slide is expected wealth minus gamma over two times the variance, where gamma is a positive number that says how much you dislike variance compared with mean. A more risk-averse investor has a higher gamma.

MIGUEL: So gamma is my personal fear coefficient. Mine is high, I just picked the sure hundred thousand.

MEI: That's section zero done. Section A is the heart of the lecture.

## A. Two stocks: the effect of diversification

MEI: The claim, in bold with three exclamation marks on the slide, because Professor Saldarriaga was clearly excited about it: the appropriate combination of stocks can produce an investment with lower risk. This is extremely powerful and important.

MIGUEL: Three exclamation marks. He means it.

MEI: The intuition: investing in stocks that co-move in opposite directions reduces the risk. The example is fifty euros in Umbrella Inc and fifty in Sun Umbrella Inc. One does well when it rains, the other when it shines, and together they're calm.

MIGUEL: And the more realistic example?

MEI: A table from the textbook with three fictitious stocks over six years, 2013 to 2018: North Air, West Air and Tex Oil. All three have the same average return, ten percent, and the same volatility, thirteen point four percent. On their own they're identical.

MIGUEL: And in pairs?

MEI: Half in North Air and half in West Air: average return still ten percent, volatility twelve point one. A bit lower. Half in West Air and half in Tex Oil: average return still ten percent, volatility five point one percent.

MIGUEL: From thirteen point four to five point one, with the same return. Just by picking the oil company instead of the second airline.

MEI: Because the two airlines move together, and the airline and the oil company move apart. When oil is expensive, the airline suffers and the oil firm thrives. To measure "move together" we need the three monsters.

## The three monsters: covariance, correlation, beta

MEI: The slide says: but first, let's face three monsters that we will need here. Covariance, correlation, beta. Three key concepts to understand how stocks move in relation to each other. And here we do what we promised: intuition in words, the formulas are on the slides.

MIGUEL: Monster one.

MEI: The covariance asks one question: when one stock does better than usual, does the other one do better than usual too? The recipe: for each year, measure how far stock i landed from its own average, do the same for stock j, multiply the two distances, then average over the years. That's one formula on the slide, with our friend the summation sign and a T minus one.

MIGUEL: How do I read the result?

MEI: Think about the sign of each product. Both above their average, or both below: same sign, positive product, pushes the covariance up. One above while the other is below: negative product, pushes it down. So a positive covariance means the two stocks tend to move together, a negative one that they move in opposite directions, and near zero, no systematic link.

MIGUEL: And the size?

MEI: Only the sign is easy to read. The size depends on the units, which is why we rescale it into the correlation. One more variant on the slides: when you have scenarios instead of past years, a boom, a normal year, a recession, each with its probability, you weight each scenario by its probability instead of counting every year equally. Same idea, different weights. The formula is on the "covariance with scenarios" slide.

MIGUEL: Monster two, the correlation.

MEI: Divide the covariance by the two volatilities. The units cancel and the result is always between minus one and plus one. Plus one: the two always move together, in perfect step. Zero: no systematic link. Minus one: when one goes up the other goes down, every time. Same information as the covariance, on a scale we can read. There's a picture on the slide with scatter plots for several correlations, worth a look.

MIGUEL: Monster three, the beta.

MEI: The beta answers a different question: when X moves by one percent, by how much does Y move on average? It's the covariance divided by the variance of X, the one that does the moving. If X is the whole market, the beta says how sensitive the stock is to the market. A beta of one point five: a market rise of one percent comes with a rise of about one point five percent for that stock, and a fall of one percent with a fall of about one point five. Above one amplifies the market, below one dampens it, negative moves against it.

MIGUEL: And the slide says beta comes back.

MEI: As the central measure of risk in lecture four, the CAPM. Then there's a table with the three side by side, and the professor's summary line is the one to remember: all three are built from the same covariance. They only differ in what we divide it by: nothing for the covariance itself, the two volatilities for the correlation, the variance of X for the beta. And covariance and correlation always have the same sign.

MIGUEL: Can we see one computed?

MEI: The textbook table does it for the airlines and the oil company. Covariance between North Air and West Air: zero point zero one one two, positive. Between West Air and Tex Oil: minus zero point zero one two eight, negative. Correlations: zero point six two four for the two airlines, minus zero point seven one three for the airline and the oil firm.

MIGUEL: So the airlines are strongly positive, the airline and oil are strongly negative. That's why the second portfolio was so calm.

MEI: And then a table of real stocks: Microsoft, HP, Alaska Air, Southwest Airlines, Ford, Kellogg, General Mills. Volatilities from seventeen percent for General Mills to forty-seven for Ford. And look at the correlations: the two airlines, zero point four. Microsoft and HP, zero point four. Kellogg and General Mills, two cereal makers, zero point five five, the highest in the table. Microsoft and Kellogg: zero point zero four.

MIGUEL: Firms in the same business move together. Software and breakfast cereal have nothing in common.

MEI: That's the lesson of that table. Same industry, high correlation, little diversification. Different industries, low correlation, lots of it.

## The risk of a portfolio with two stocks

MEI: Now the main formula of the lecture, and again, intuition here, equation on the slide. There's first a reminder slide on properties of the covariance, that it's bilinear and that the variance is a covariance of a thing with itself. You can read it; it's what makes the next step work.

MIGUEL: Which is?

MEI: The return of a portfolio is a weighted average of the two returns. The weights are the fraction of your money in each stock, and they add up to one. Thirty euros of every hundred in stock one and seventy in stock two means weights of zero point three and zero point seven.

MIGUEL: And the risk?

MEI: The variance of the portfolio has three pieces. The first weight squared times the variance of stock one. The second weight squared times the variance of stock two. And then two times the first weight times the second weight times the covariance between the two stocks. The slide also writes that last piece with the correlation times the two volatilities, which is the same thing. The volatility of the portfolio is the square root of all that.

MIGUEL: So the risk of a portfolio is not the sum of the individual risks.

MEI: The slide says exactly that, in bold: not the sum. It's the individual risks plus the comovement. If the stocks co-move in opposite directions, the covariance term is negative and the aggregated risk is smaller. If they co-move in the same direction, it's greater.

MIGUEL: And the three boxes about correlation?

MEI: Three cases, worth memorizing. Correlation equal to one: the portfolio volatility is just the weighted average of the two volatilities. No diversification at all. Correlation below one: the portfolio volatility is smaller than that weighted average. That gap is the effect of diversification. Correlation equal to minus one: the portfolio volatility is the absolute value of the difference between the weighted risks, and with the right weights you can bring it to zero.

MIGUEL: So anything below a correlation of one helps, and the lower the better.

MEI: Then there's a slide for N stocks, with a double summation sign, and the professor wrote "don't panic" on it: we will not use this formula for more than two stocks. So: don't panic.

MIGUEL: He said don't panic, I'm not panicking.

## Short sales: can a weight be negative?

MEI: One more concept before the worked example. So far every weight was between zero and one. A weight can also be negative. It means you sold a stock you do not own: a short sale.

MIGUEL: How do you sell something you don't own?

MEI: You borrow the share, in practice from your broker, sell it today, and buy it back later to give it back. You hold the cash now and owe one share later. You gain if the price falls: sell at a hundred, buy back at sixty, return the share, keep forty. You lose if it rises: buying back at a hundred and fifty costs you fifty.

MIGUEL: The slide has a soccer ticket.

MEI: A friend lends you a match ticket and says "give it back next month." You think tickets will be cheaper, so you sell it today for a hundred euros. Next month tickets cost sixty: you buy one, hand it back, keep the forty. You made money on a ticket you never owned. If tickets had gone to a hundred and fifty, you'd still have to buy one to return it, and lose fifty.

MIGUEL: Two lessons, I think the slide says.

MEI: A short position wins when the price goes down and loses when it goes up. And there is no ceiling on the loss, because a price can keep rising.

MIGUEL: And in the portfolio formula?

MEI: You have a hundred euros. You short fifty euros of stock one and put all the cash you now hold, your hundred plus the fifty raised, into stock two. The weights are minus zero point five and one point five. They still add up to one, since the money always comes from somewhere. The formulas don't change: if stock one falls, the negative weight turns that fall into a gain. Lecture three uses negative weights to widen the set of portfolios you can build.

## The worked example: two stocks, four years

MEI: And now the part of the lecture built for the exam: six steps, by hand. Two stocks, A and B, four years of returns. Stock A: twelve, minus four, ten, two percent. Stock B: one, nine, minus three, five percent.

MIGUEL: A's best years are B's worst.

MEI: Which is the point. Step one, mean returns. A: twelve minus four plus ten plus two is twenty, over four, five percent. B: one plus nine minus three plus five is twelve, over four, three percent.

MIGUEL: Step two.

MEI: Variances and volatilities. Take each year's distance to the mean, square it, add up. For A the distances are seven, minus nine, five, minus three. Squares: forty-nine, eighty-one, twenty-five, nine. Sum: a hundred and sixty-four. Divide by T minus one, three: fifty-four point seven. Square root: a volatility of seven point four percent.

MIGUEL: And B?

MEI: Distances minus two, six, minus six, two. Squares four, thirty-six, thirty-six, four. Sum eighty. Over three: twenty-six point seven. Volatility five point two percent.

MIGUEL: Step three, the covariance.

MEI: Same distances, but multiply A's by B's, year by year. Seven times minus two, minus fourteen. Minus nine times six, minus fifty-four. Five times minus six, minus thirty. Minus three times two, minus six. Sum: minus a hundred and four. Over three: minus thirty-four point seven.

MIGUEL: Every product is negative.

MEI: Every single one. In each year, when one stock is above its average the other is below. Step four, the correlation: minus thirty-four point seven divided by seven point four times five point two, that's thirty-eight point two: minus zero point nine one. Close to minus one, the two stocks move almost perfectly against each other.

MIGUEL: And the beta?

MEI: Beta of B with respect to A: the covariance over the variance of A. Minus thirty-four point seven over fifty-four point seven: minus zero point six three. When A goes up by one percent, B goes down by about zero point six three percent on average.

MIGUEL: Step five, the portfolio.

MEI: Half the money in each. Year by year the portfolio earns the average of the two returns: six point five, two point five, three point five, three point five. Mean: four percent. Which is exactly what the formula gives: half of five plus half of three.

MIGUEL: And step six, the risk. This is the moment of truth.

MEI: With the formula: a quarter of fifty-four point seven, thirteen point seven. Plus a quarter of twenty-six point seven, six point seven. Plus two times a half times a half times minus thirty-four point seven, that's minus seventeen point three. Total: three point zero. Square root: one point seven percent.

MIGUEL: One point seven. From seven point four and five point two.

MEI: And the slide checks it directly on the portfolio returns: the distances to the four percent mean are two point five, minus one point five, minus zero point five, minus zero point five; their squares add up to nine, and nine over three is three. Same answer.

MIGUEL: So the negative covariance term ate most of the risk, and the return stayed a plain average of the two.

MEI: That's the takeaway on the last slide, word for word: that is diversification at work.

MIGUEL: Professor Saldarriaga really went far on this one. Six steps, two tables, and a check at the end. I don't think anyone can say they didn't see the exam coming.

MEI: That's the idea. Do it once by hand with the slides open, and the three monsters stop being monsters.

## Wrap-up: the recap

MIGUEL: Okay. Recap time. The whole lecture in one minute.

MEI: The recap of lecture one: returns compound, average them with the geometric mean, expect them with the arithmetic mean, and risk is volatility, the standard deviation of returns. Big portfolios are rewarded for risk, single stocks are not, and this lecture explains why.

MIGUEL: The framework.

MEI: People prefer a sure hundred thousand to a fair coin flip for two hundred thousand: that's risk aversion. So we describe every investment by two numbers, expected return and variance, and investors want more of the first and less of the second. A utility function scores that trade-off, with gamma as the degree of risk aversion.

MIGUEL: The monsters.

MEI: Covariance: do two stocks move together? Its sign is what you read. Correlation: the covariance rescaled between minus one and plus one. Beta: how much Y moves when X moves one percent. All three are the same covariance divided by different things. Same industry, high correlation; cereal and software, almost none.

MIGUEL: The portfolio.

MEI: Portfolio return is the weighted average of returns. Portfolio variance is the two weighted variances plus a comovement term with the covariance. Correlation of one, no diversification; below one, the portfolio is less risky than the average; minus one, you can cancel the risk entirely. Weights can be negative: that's a short sale, which wins when the price falls and has no ceiling on the loss.

MIGUEL: And the example.

MEI: Stock A, five percent return and seven point four volatility. Stock B, three percent and five point two. Correlation minus zero point nine one. Half and half: four percent return, one point seven percent volatility. Diversification at work.

MIGUEL: My takeaway: never ask how risky a stock is on its own. Ask how it moves with the rest of what you own.

MEI: Redo the six steps with a calculator, look at the formulas on the slides while you listen to this again, and read chapters 10.5, 10.6 and 11.1. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you in the next lecture.
