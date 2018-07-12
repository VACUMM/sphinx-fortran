module assim

contains

subroutine utl_matsqrt(PA,KN,ZSIGN,printInformation_opt)
    !
    ! Calculate square root of an error covariance matrix
    !
    implicit none
    INTEGER, intent(in)           :: KN ! order of the matrix
    REAL(8), intent(inout)        :: PA(KN,KN) ! on entry, the original matrix; on exit, the sqrt matrix
    REAL(8), intent(in)           :: ZSIGN ! sign of the exponent
    LOGICAL, intent(in), optional :: printInformation_opt ! request more verbose output

    call extfunc(pa)

end subroutine utl_matsqrt

end module assim
