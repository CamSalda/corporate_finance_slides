# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture 12: Options and Risk Management

> **Lecture companion.** This episode walks through Lecture 12 of the Corporate Finance course at ESCP Business
> School (Camilo Saldarriaga, 2026/2027), which covers chapter 20 of Berk and DeMarzo. It is made with the
> open-source tools of The Finance and Economics Papers Podcast, for the students of the course. All numbers
> and examples come from the lecture slides.

- **Lecture:** Corporate Finance, Lecture 12: Options and Risk Management. ESCP Business School, 2026/2027.
- **Textbook:** Berk, J., & DeMarzo, P. *Corporate Finance*, chapter 20.
- **Topics:** Recap of long-term financing; risks and hedging; derivatives; forwards and futures; Ryanair's fuel hedge; an exporter's currency hedge; calls and puts; option terminology and moneyness; the max notation; payoffs at expiration for buyers and sellers; Black-Scholes in words; option exchanges; reading an option quote; profit and return on a call; portfolio insurance; farewell to the course
- **Length:** 25 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Today is a special format, and a special day. Instead of a paper, we walk through a lecture: Lecture 12 of the Corporate Finance course at ESCP, "Options and Risk Management." It follows chapter 20 of the Berk and DeMarzo textbook, and every number we mention comes from the slides.

MIGUEL: Lecture twelve. The last one.

MEI: The last one, and a short one on purpose: the second half of the session is the final exam briefing, which has its own deck. So today's plan has three sections. A, futures and forwards, the simplest derivatives. B, option basics. C, option payoffs at expiration. And at the end, a look back at the whole course.

MIGUEL: Equations?

MEI: Eight formula blocks in the deck, and seven of them are the same thing: "take the bigger of two numbers." The eighth is Black-Scholes, and the professor himself put a slide called "Black-Scholes without the maths" right after it, so we'll do the same. Everything else is tables with small numbers, which we'll read aloud.

MIGUEL: Recap first.

## Recap of lecture eleven

MEI: Four recap slides. Raising equity: private firms raise money in funding rounds, where the post-money value is the pre-money value plus the money invested, and the new investors own money invested over post-money. The IPO: the first sale of shares to the public, run by an underwriter who sets the price through book building, can sell extra shares through the greenshoe, and keeps insiders locked up for months. Three facts: IPOs are underpriced on average, they come in waves, and they do poorly in the long run.

MIGUEL: SPACs and seasoned offerings.

MEI: A SPAC is a listed shell full of cash that merges with a private firm, a back door to the market, cheaper and faster than an IPO and poor on average. A seasoned equity offering is a listed firm selling new shares: a cash offer to anyone, where a low price moves wealth from old to new shareholders, or a rights offer to existing shareholders, where the value stays with them. The price falls on the announcement because investors read a sale as a sign that managers think the shares are expensive.

MIGUEL: Debt.

MEI: Private debt, bank loans and placements, or public bonds. Seniority: secured, then senior unsecured, then subordinated, with higher rates further down the ladder. Covenants, promises in the bond contract that protect lenders and lower the rate. And sovereign bonds, TIPS, asset-backed securities and CDO tranches.

MIGUEL: And bonds with options.

MEI: Callable: the firm may repay early, the right belongs to the firm, so investors ask for a higher yield. Puttable and convertible: the investor may ask for early repayment or swap the bond for shares, so the investor accepts a lower yield. And the last line of the recap is the door into today: last week the options were hidden inside bonds. Today we open the box and study the option itself.

## Introduction

MEI: A company is exposed to many risks: changes in demand, in the cost of commodities, loss of key employees, new competitors, operational risks. The important question: should investors bear these risks, or should the company reduce them? Managers have two tools: prevention, and hedging, either with insurance contracts or in financial markets.

MIGUEL: Insurance versus derivatives.

MEI: Some risks are easy to insure: accidents, illness, fire. For others it's hard or impossible to find insurance: climate risk, natural disasters, the cost of commodities. And in particular, a risk that is hard to diversify is usually easier to hedge with a financial derivative than with an insurance contract. A derivative is a contract whose value depends on another value, the underlying. The professor's phrase: think of it as a side bet whose value is read off another price. Examples: credit default swaps, swaps, futures and forwards, options.

## A. Futures and forwards

MEI: A forward is a legal agreement between a buyer and a seller: the buyer agrees to buy something at a specified price on a specified date, the seller agrees to sell it. A market for standardised forwards with a clearing house is a futures market: there are margin requirements, and the clearing house is the counterparty to everyone, so there's no credit risk.

MIGUEL: Why does a clearing house remove the credit risk? Somebody still has to pay.

MEI: Somebody does, but you never have to wonder who. In a plain forward, if the other side goes bankrupt before the date, your hedge disappears with them. In a futures market, you face the clearing house, not the other trader, and the clearing house protects itself with margins: every day, whoever is losing on the contract tops up a deposit. So when the date comes, the money is already there. Same economics as a forward, much safer plumbing.

MIGUEL: The step-by-step example.

MEI: An airline agrees today to buy jet fuel in three months at a forward price of a hundred per unit. No money changes hands today. In three months, the airline pays a hundred whatever the spot price is. If the spot price is eighty, the buyer pays a hundred for fuel worth eighty: a loss of twenty, and the seller gains twenty. At a hundred, nobody gains. At a hundred and twenty, the buyer pays a hundred for fuel worth a hundred and twenty: a gain of twenty, and the seller loses twenty.

MIGUEL: So one side's gain is the other side's loss.

MEI: And both sides can lose. The contract fixes the price today, so the price risk moves from the buyer to the seller. The terminology table: spot means buy today at today's price; forward means agree today, trade later at the forward price, on the expiration date. The buyer has the long position and must buy; the seller has the short position and must sell. The thing traded is the underlying.

MIGUEL: And Ryanair.

MEI: The real-life slide, from the Guardian. "European air fares could rise by as much as twenty percent in 2027, Ryanair boss predicts." Conflict in the Middle East pushed jet fuel up, and many carriers were not hedged. Ryanair had hedged 2026: eighty percent of its fuel locked in at sixty-seven dollars a barrel before the Iran conflict. But 2027 was mostly not hedged: only fifteen percent locked in, at eighty-five dollars, with the spot price about double.

MIGUEL: So the hedge protects you exactly as far as it goes.

MEI: A hedge fixes the price only for the quantity and the dates it covers. That's why fares could still rise by up to twenty percent. The professor really went out and found a headline from this year for a slide that used to be just a table. Nice touch.

MIGUEL: The value of a forward.

MEI: The payoff figure. For the buyer, the long side: above a hundred, you pay a hundred for something worth more, you gain; below a hundred, you could have bought cheaper, you lose. A straight line through a hundred. The seller is the mirror image. The buyer profits if the underlying rises, the seller if it falls. Futures usually expire in March, June, September and December, and you can close a position before expiry by taking the opposite one on the same contract. At maturity, settlement is in cash, for a stock index for example, or by physical delivery, for bonds or commodities.

MIGUEL: The wine exporter.

MEI: A French wine maker sells to a US importer and will receive one point one million dollars in three months. Today one euro is one dollar ten, so that's worth one million euros. The risk: if the dollar weakens, the same dollars buy fewer euros. The hedge: sign a forward today to sell one point one million dollars in three months at one dollar ten, the short position on dollars.

MIGUEL: The table.

MEI: If in three months one euro is one dollar, without the forward the exporter gets one point one million euros; at one ten, one million; at one twenty-five, zero point eight eight million. With the forward: one million, one million, one million. The forward fixes the euros it will receive. It gives up the gain if the dollar strengthens, in exchange for no loss if it weakens.

MIGUEL: Which is exactly the problem with forwards.

MEI: Which is exactly the bridge to section B.

## B. Option basics

MEI: The major drawback of forwards and futures is the possibility of a negative payoff. A forward that does not force the two parties to execute is called an option. So an option is a forward with a payoff that is never negative. And because an option is a bet in which you cannot lose, you have to pay to enter it: the premium.

MIGUEL: Let me put the wine maker back in. With the forward, she gave up the gain if the dollar strengthened. With an option?

MEI: With a put option on dollars at one ten, she keeps the right to sell at one ten if the dollar weakens, and she simply doesn't use it if the dollar strengthens: she sells her dollars in the market at the better rate. Floor on the downside, upside kept. And for that she pays a premium today, which the forward never asked for. That's the trade in one sentence: a forward is free and symmetric, an option costs money and is one-sided.

MIGUEL: Call and put.

MEI: A call gives the owner the right, but not the obligation, to buy a fixed quantity of the underlying at a certain price, the strike or exercise price, at or before a certain date, the expiration date. A put gives the right to sell at the strike. The premium is paid by the buyer to the seller to acquire the right. And a reminder with three exclamation marks on the slide: the greenshoe from lecture eleven is a call option. For about thirty days after the IPO, the underwriter has the right to buy extra shares from the firm at the offer price.

MIGUEL: Three exclamation marks. Down from five in lecture seven.

MEI: He's pacing himself for the exam. The side-by-side table: a call is the right to buy at the strike, used when the share is above it, the buyer gains when the price rises. A put is the right to sell at the strike, used when the share is below it, the buyer gains when the price falls. Both buyers pay the premium today. The call seller must sell at the strike if asked; the put seller must buy at the strike if asked. The premium is the price of a right; the seller is paid today to take on an obligation for later.

MIGUEL: Terminology.

MEI: Exercising is enforcing the agreement. The buyer, or holder, has the long position and the right to exercise. The seller, or writer, has the short position and the obligation to fulfil the contract if it's exercised. Intrinsic value is the gain from exercising right now. At the money: strike equal to the current price. In the money: exercising now would pay. Out of the money: exercising now would lose. Deep in or out of the money: strike and price far apart.

MIGUEL: And the continents.

MEI: European options can be exercised only on the expiration date; American options on any date up to and including it. And the slide warns: the names have nothing to do with where the options trade. Then Asian options, based on an average, for instance the average monthly return of the CAC 40 over five years; and Bermuda options, exercisable only on specific dates.

MIGUEL: Bermuda. Somewhere between Europe and America, like the exercise rule.

MEI: That is in fact where the name comes from. One consequence worth a second: an American option gives you everything a European one does, plus extra dates to exercise, so it can never be worth less than the European one with the same strike and expiry. More rights, higher or equal price. Then who expects what: the buyer of a call expects the price to rise, the seller of a call expects it to fall, the buyer of a put expects it to fall, the seller of a put expects it to rise. And the table of who gains: buy a call, gain when the price rises, lose only the premium when it falls. Sell a call, lose without limit when it rises, keep the premium when it falls. Buy a put, lose only the premium when it rises, gain when it falls. Sell a put, keep the premium when it rises, lose up to the strike when it falls. The buyer of an option can never lose more than the premium. The seller keeps the premium when nothing happens, and pays when the buyer exercises.

## The max block

MEI: Now four slides that the professor built for one piece of notation, and I think they're the most thoughtful slides in the deck. The formulas coming up contain "max of S T minus K and zero." Max of two numbers means: look at both and keep the bigger one. Nothing else. Max of three and seven is seven, in either order. Max of minus five and zero is zero: when one of the two is zero, a negative number never wins. So "max of something and zero" is just a way of writing "never let this go below zero."

MIGUEL: Four slides to say "keep the bigger number."

MEI: And they're worth it, because that one word is the entire difference between a forward and an option. At expiration, the holder chooses whether to use the option. Nobody chooses to lose money, so it's used only when it pays. Take a call with a strike of twenty, the right to buy the share for twenty. If the share is worth twenty-five, you buy at twenty something worth twenty-five: you gain five. If it's worth fifteen, buying at twenty is a bad deal, so you walk away and get zero. "Take the better of the two" is exactly what max writes down: the call payoff is max of the share price minus twenty and zero.

MIGUEL: The numbers table.

MEI: Strike twenty. Share price at expiration ten, fifteen, twenty, twenty-five, thirty. Share minus strike: minus ten, minus five, zero, five, ten. Call payoff: zero, zero, zero, five, ten. Put payoff, max of strike minus share and zero: ten, five, zero, zero, zero.

MIGUEL: And that's why the graph has an elbow.

MEI: On the flat part, max is picking the zero: the option isn't worth using. On the sloped part, max is picking share minus strike: every extra euro on the share is an extra euro of payoff. The two parts meet at the strike. That's the kink.

## C. Option payoffs at expiration

MEI: Section C states it formally. The value of a call at expiration is max of S T minus K and zero, where S T is the price of the underlying at expiration and K the strike. The figure for a strike of twenty: flat at zero up to twenty, then rising one for one. The put: max of K minus S T and zero, falling one for one from the strike down to zero, flat after.

MIGUEL: The seller's side.

MEI: Whatever the buyer receives, the seller pays, so the seller's payoff is minus the buyer's. Same table, strike twenty, share ten to thirty. Buyer of the call: zero, zero, zero, five, ten. Seller of the call: zero, zero, zero, minus five, minus ten. Buyer of the put: ten, five, zero, zero, zero. Seller of the put: minus ten, minus five, zero, zero, zero. And a point to remember: the seller of a put can lose at most the strike, because the share can't fall below zero. The seller of a call has no floor, because the share can rise without limit.

MIGUEL: Black-Scholes.

MEI: The baseline slide has the full formula: the call price equals the share price times N of d one, minus the strike discounted at the risk-free rate times N of d two, with d one and d two defined by a logarithm, the volatility and the time to expiration. We won't read it; it's on slide 35 and it stays there. The professor added "Black-Scholes without the maths," and here it is. Call price equals what you may receive minus what you may pay. You may receive the share, worth S. You may pay the strike, at expiration, so it's discounted. Each piece is weighted by a number between zero and one, N of d one or N of d two, which plays the role of a probability. The remarks on the formula slide: N of d two is the risk-neutral probability that the call ends in the money, and N of d one is the delta, how much the option price moves when the share moves.

MIGUEL: And the five inputs.

MEI: The table to memorise. Share price up: the call price rises, more to gain. Strike up: falls, you pay more to exercise. Time to expiration up: rises, more time for the share to move. Volatility up: rises, bigger gains possible while the downside is capped at zero. Risk-free rate up: rises, paying the strike later costs less today. Five inputs, five directions.

MIGUEL: Volatility makes the option more valuable. That's the one that surprises people.

MEI: Because for a share, volatility is risk, and risk is bad. For an option, volatility is opportunity on the upside with the downside already cut off at zero by the max. Same word, opposite feeling.

## History, exchanges, and the quote

MEI: Options have existed for a long time but took off in 1973, when two things happened: the first regulated options market opened, the Chicago Board Options Exchange, and two academic articles pioneering option pricing were published, Black and Scholes among them. A large number of options still trade over the counter rather than on exchanges.

MIGUEL: And in Europe.

MEI: The deck has a fresh slide on where options trade today. Eurex in Frankfurt, created in 1998 from the German and Swiss futures exchanges, owned by Deutsche Börse, known for the Euro-Bund futures on ten-year German bonds and for futures and options on the Euro Stoxx 50 and the DAX. ICE Futures Europe in London, the former LIFFE: opened in 1982, bought by Euronext in 2002, NYSE Liffe in 2007, part of the US group ICE since 2013; Euribor futures, FTSE 100 options, cocoa, coffee and sugar. And Euronext in Paris, independent again since 2014, with the futures and options on the CAC 40. All three work as section A described: an electronic order book, standardised contracts, a clearing house between buyer and seller.

MIGUEL: The quote exercise.

MEI: A CBOE quote table for eBay, 10 September 2018, share at thirty-three seventy-five. Calls on the left, puts on the right, each with last sale, bid, ask, volume and open interest. You decide to buy the call with a strike of thirty expiring in January. Two questions: is it in or out of the money, and what's your return if you hold it to expiry and the share ends at forty?

MIGUEL: Step one.

MEI: Moneyness. The share trades at thirty-three seventy-five and the strike is thirty. The right to buy at thirty something worth thirty-three seventy-five is worth using: in the money, intrinsic value three seventy-five. Step two, the cost: a buyer pays the ask price, four dollars eighty.

MIGUEL: Why the ask and not the bid? The table shows four seventy and four eighty.

MEI: Because the bid is what buyers in the market are offering, and the ask is what sellers are asking. When you buy, you take the seller's price: the ask. When you sell, you get the bid. The ten cents between them is the dealer's margin, and it's a real cost: buy at four eighty and sell straight back at four seventy and you've lost ten cents for nothing. Notice also that four eighty is more than the intrinsic value of three seventy-five. The extra dollar and five cents is time value: the market pays for the chance that eBay rises further before January. Step three, the payoff if the share is at forty: max of forty minus thirty and zero, ten. Step four, the profit: payoff minus premium, ten minus four eighty, five twenty. Step five, the return: profit over cost, five twenty over four eighty, a hundred and eight point three three percent.

MIGUEL: Compared with just buying the share?

MEI: Forty over thirty-three seventy-five minus one: eighteen point five two percent. Same news, about six times the return. An option is a leveraged bet. And the other side of that coin: if the share ends below thirty, the option expires worthless. A return of minus one hundred percent.

MIGUEL: The profit figure.

MEI: Each line is a call with a different strike, from thirty to forty. Below the strike you lose what you paid. Above it, every extra dollar on the share is an extra dollar of profit. A low strike costs more but pays sooner; a high strike costs less but needs a bigger rise. The lines start at different depths below zero, the premiums, and cross each other as the share rises.

## Portfolio insurance

MEI: The last application. Options can protect a portfolio against a fall. An investor holds only Amazon shares, worries the price may drop, but doesn't want to sell because it might also rise. Two ways to insure against the price falling below forty-five dollars, in the textbook's figure.

MIGUEL: Way one.

MEI: Keep the shares and buy a European put with a strike of forty-five. Below forty-five the put pays the difference, so the combination is flat at forty-five; above it, you ride the share up. The orange line is a floor at forty-five with the full upside.

MIGUEL: Way two.

MEI: Buy a risk-free zero-coupon bond that pays forty-five at expiration, plus a European call on Amazon with a strike of forty-five. Below forty-five you have the bond, forty-five; above it, the call adds the rise. The same orange line, built from different pieces. Share plus put equals bond plus call. That identity, put-call parity, is the one line to remember from this slide, and it's what the Black-Scholes slide meant by "a similar formula for puts."

## What to remember

MEI: Three lines, one per section. A, forwards and futures: a promise to buy or sell at a fixed price on a fixed date, no premium, both sides can lose, and futures are standardised forwards with a clearing house. B, options: a right, not an obligation. A call is the right to buy at the strike, a put the right to sell. The buyer pays a premium, the seller is paid to take on an obligation. In, at or out of the money; European or American. C, payoffs: call, max of S T minus K and zero; put, max of K minus S T and zero; the seller's payoff is the mirror image; profit is payoff minus premium; and share plus put equals bond plus call.

## Wrap-up: the recap, and the course

MEI: Lecture twelve in one minute. Companies face risks they can prevent, insure, or hedge in the markets. A forward fixes a price today for a trade later: the jet fuel at a hundred, the exporter's dollars at one ten. Both sides can lose, and the hedge covers only what it covers, as Ryanair's 2027 shows. An option is a forward you may walk away from, so it never pays less than zero, and that's why you pay a premium for it. Max of two numbers is the whole trick: the payoff of a call is the bigger of share minus strike and zero, a put the bigger of strike minus share and zero, and the seller gets the mirror image. Black-Scholes prices a call as what you may receive minus what you may pay, weighted by probabilities; share up, time up, volatility up and rates up all raise it, a higher strike lowers it. The eBay January 30 call: in the money, four eighty to buy, ten of payoff at forty, a hundred and eight percent return, or minus a hundred if it ends below thirty. And a share plus a put is a bond plus a call: portfolio insurance.

MIGUEL: The quiz.

MEI: Does the holder have to exercise? No: a right, not an obligation; the seller is the one who must deliver if asked. Portfolio insurance with puts: keep the shares and buy a put with the floor as its strike; with calls: buy a risk-free bond paying the floor plus a call with the same strike. And the January 30 call at four eighty with the share at thirty-two: payoff two, profit two minus four eighty, minus two eighty, return minus fifty-eight point three three percent. In the money, and you still lost money. The premium matters.

MIGUEL: And that's the course.

MEI: That's the course. Twelve lectures. We learned to price risk and saw that only the risk you can't diversify is paid, lectures one to four. We asked whether anyone can beat the market, lecture five, and how to estimate the cost of capital, lecture six. Then Modigliani and Miller, three times: in a perfect market, how you finance a project changes nothing, seven and eight; taxes make debt valuable up to a point, nine; and dividends are irrelevant until taxes, cash and signals make them matter, ten. We raised money in lecture eleven, and today we learned how to protect it.

MIGUEL: My takeaway for the whole course: every lecture had a fallacy, and every fallacy was someone forgetting that risk has a price. Also, Intel and Coca-Cola deserve an honorary ESCP degree.

MEI: Read chapter 20, redo the eBay quote with the January 35 call, and then go through the final exam deck. Thank you for listening to all twelve companions of The Finance and Economics Papers Podcast. Good luck on the exam.

MIGUEL: You'll do great. See you in the next course.
