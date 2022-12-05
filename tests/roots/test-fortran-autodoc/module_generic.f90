module generic
! A module of generic utilities

integer, parameter :: nens = 100 ! Size of the ensemble
real, dimension(nens) :: sst, & ! Sea surface temperature
    & sss ! Sea surface salinity
integer, private :: numberOfFish

type mytest
    ! Description of my type
    !
    ! : Parameters:
    ! - **arr2**: Array described in docstring

    integer :: myint ! Description of myint
    real(kind=4) :: arr(10), &! Array of fixed size
        & arr2(20)

end type mytest

type mysecondtest
    ! Description of my second type

end type mysecondtest

private :: feedFish
public :: evolve

contains

  subroutine evolve()
    call feedFish()
  end subroutine evolve

  subroutine feedFish()
    numberOfFish = numberOfFish + 1
  end subroutine feedFish

end module generic
