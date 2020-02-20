subroutine calc_distance (np, nd, pos, i, j, rij, d, d2)
!
!  Calculate Distance vector, scalar distance and trucated distance
!  between atoms i and j.
!  The distance is truncated at pi/2
!
    implicit none
    integer(kind=4),intent(in) :: np                ! number of particles
    integer(kind=4),intent(in) :: nd                ! number of dimensions
    real(kind=8),intent(in),dimension(nd,np) :: pos ! positions
    integer(kind=4),intent(in) :: i                 ! index particle I
    integer(kind=4),intent(in) :: j                 ! index particle J
    real(kind=8),intent(out),dimension(nd) :: rij   ! distance vector
    real(kind=8),intent(out) :: d                   ! distance
    real(kind=8),intent(out) :: d2                  ! trucated distance

    real ( kind = 8 ), parameter :: PI2 = 3.141592653589793D+00 / 2.0D+00

    rij(1:nd) = pos(1:nd,i) - pos(1:nd,j)

    d = sqrt ( sum ( rij(1:nd)**2 ) )

    !  Truncate the distance:
    d2 = min ( d, PI2 )
end subroutine calc_distance