module generic
! A module of generic utilities

integer, parameter :: nens = 100 ! Size of the ensemble
real, dimension(nens) :: sst, & ! Sea surface temperature
    & sss ! Sea surface salinity

type mytest
    ! Description of my type
    !
    ! : Parameters:
    ! - **arr2**: Array described in docstring

    integer :: myint ! Description of myint
    real(kind=4) :: arr(10), &! Array of fixed size
        & arr2(20)

end type mytest

end module generic