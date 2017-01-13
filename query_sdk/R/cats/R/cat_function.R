pkg.env <- new.env()
pkg.env$love_state <- 10

#' A Cat Function
#'
#' This function allows you to express your love of cats.
#' @param love Do you love cats? Defaults to TRUE.
#' @keywords cats
#' @export
#' @examples
#' cat_function()

cat_function <- function(love=TRUE){
    if(love==TRUE){
	pkg.env$love_state <- pkg.env$love_state + 1
	print("I love cats!")
    }
    else {
	pkg.env$love_state <- pkg.env$love_state - 1
        print("I am not a cool person.")
    }
}

#' Access Function
#'
#' This function allows you to check on the state of love for cats.
#' @keywords cats
#' @export
#' @examples
#' get_love_state()
get_love_state <- function(){
	print(paste("Love in the world is at",pkg.env$love_state," degrees"))
	#print("foobar")
}
